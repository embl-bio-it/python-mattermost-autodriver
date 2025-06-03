import ast
import os

from subprocess import run
from typing import Callable


class ASTEndpointParser:
    def __init__(
        self,
        endpoints_dir: str,
        base_driver_class_name: str,
        driver_file_path: str = os.path.join("driver", "endpoint_base.py"),
        modify_module_class_name: Callable[[str], str] | None = None,
    ):
        module_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            os.pardir,
            "src",
            "mattermostautodriver",
        )

        self.base_driver_class_name = base_driver_class_name
        self.driver_file_path = os.path.join(module_path, driver_file_path)
        self.endpoints_dir = endpoints_dir
        self.endpoints_path = os.path.join(module_path, endpoints_dir)
        self.modify_module_class_name = modify_module_class_name

    def parse_file(self) -> ast.Module:
        """Parse the Python file and return the AST."""
        with open(self.driver_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return ast.parse(content)

    def discover_all_endpoints(self) -> list[tuple[str, str]]:
        """
        Discover all endpoint modules from the filesystem.

        Returns:
            list of tuples (module_name, class_name)
        """
        if not os.path.exists(self.endpoints_path):
            raise FileNotFoundError(f"Endpoints directory not found: {self.endpoints_path}")

        endpoints = []

        for endpoint in os.listdir(self.endpoints_path):
            if not endpoint.endswith(".py"):
                continue

            module_name = os.path.splitext(os.path.basename(endpoint))[0]
            if module_name.startswith("_"):
                # Skip base endpoint and any other file starting with _ (e.g. __init__)
                continue

            # Load module and find the main module class
            with open(os.path.join(self.endpoints_path, endpoint), "r", encoding="utf-8") as f:
                source_code = f.read()

            tree = ast.parse(source_code)

            # Walk through the AST nodes to find the first class
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_name = node.name
                    break
            else:
                raise Exception(f"Could not find class definition in {endpoint}")

            endpoints.append((module_name, class_name))

        return sorted(endpoints)  # Sort for consistent ordering

    def remove_existing_endpoint_imports(self, tree: ast.Module) -> ast.Module:
        """
        Remove all existing endpoint imports from the AST.

        Returns:
            Modified AST with endpoint imports removed
        """
        # Filter out endpoint imports
        tree.body = [
            node
            for node in tree.body
            if not (
                isinstance(node, ast.ImportFrom)
                and node.module
                and node.module.startswith(f"{self.endpoints_dir}.")
                and node.names
            )
        ]
        return tree

    def create_import_node(self, module_name: str, class_name: str) -> ast.ImportFrom:
        return ast.ImportFrom(
            module=f"{self.endpoints_dir}.{module_name}",
            names=[
                ast.alias(
                    name=class_name,
                    asname=self.modify_module_class_name(class_name) if self.modify_module_class_name else None,
                )
            ],
            level=0,
        )

    def create_assignment_node(self, module_name: str, class_name: str) -> ast.Assign:
        attr_name = module_name.lower()

        return ast.Assign(
            targets=[ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr=attr_name, ctx=ast.Store())],
            value=ast.Call(
                func=ast.Name(
                    id=self.modify_module_class_name(class_name) if self.modify_module_class_name else class_name,
                    ctx=ast.Load(),
                ),
                args=[ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr="client", ctx=ast.Load())],
                keywords=[],
            ),
        )

    def find_base_driver_with_endpoints_class(self, tree: ast.Module) -> ast.ClassDef:
        """Find the base driver class in the AST."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == self.base_driver_class_name:
                return node
        raise ValueError(f"{self.base_driver_class_name} class not found in the file")

    def find_init_method(self, class_node: ast.ClassDef) -> ast.FunctionDef:
        """Find the __init__ method in a class node."""
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == "__init__":
                return node
        raise ValueError(f"__init__ method not found in {self.base_driver_class_name} class")

    def remove_existing_endpoint_assignments(self, init_method: ast.FunctionDef) -> ast.FunctionDef:
        """Remove existing endpoint assignments from the __init__ method."""
        # Filter out endpoint assignments
        init_method.body = [
            node
            for node in init_method.body
            if not (
                isinstance(node, ast.Assign)
                and any(
                    isinstance(target, ast.Attribute)
                    and isinstance(target.value, ast.Name)
                    and target.value.id == "self"
                    and isinstance(node.value, ast.Call)
                    and isinstance(node.value.func, ast.Name)
                    and len(node.value.args) == 1
                    and isinstance(node.value.args[0], ast.Attribute)
                    for target in node.targets
                )
            )
        ]
        return init_method

    def find_super_call_index(self, init_method: ast.FunctionDef) -> int:
        """Find the index where super().__init__() is called."""
        for i, node in enumerate(init_method.body):
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                call = node.value
                # Check for super() call patterns
                if isinstance(call.func, ast.Attribute) and call.func.attr in ["__init__", "init"]:
                    if isinstance(call.func.value, ast.Call):
                        func_call = call.func.value
                        if isinstance(func_call.func, ast.Name) and func_call.func.id == "super":
                            return i + 1

        return 1  # Default to after first statement

    def update_ast(self, tree: ast.Module, discovered_endpoints: list[tuple[str, str]]) -> ast.Module:
        """
        Update the AST by removing all existing endpoint imports/assignments and adding new ones.

        Args:
            tree: The original AST
            discovered_endpoints: list of (module_name, class_name) tuples

        Returns:
            Updated AST
        """
        # Remove all existing endpoint imports
        tree = self.remove_existing_endpoint_imports(tree)

        # Create all new imports
        new_imports = [
            self.create_import_node(module_name, class_name) for module_name, class_name in discovered_endpoints
        ]

        # Find where to insert imports (after existing imports but before class definitions)
        insert_index = 0
        for i, node in enumerate(tree.body):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                insert_index = i + 1
            elif isinstance(node, ast.ClassDef):
                break

        # Insert all new imports
        for import_node in reversed(new_imports):  # Reverse to maintain order
            tree.body.insert(insert_index, import_node)

        # Update the base driver class
        class_node = self.find_base_driver_with_endpoints_class(tree)
        init_method = self.find_init_method(class_node)

        # Remove all existing endpoint assignments
        init_method = self.remove_existing_endpoint_assignments(init_method)

        # Find where to insert new assignments (after super().__init__ call)
        insert_index = self.find_super_call_index(init_method)

        # Create all new assignment nodes
        new_assignments = [
            self.create_assignment_node(module_name, class_name) for module_name, class_name in discovered_endpoints
        ]

        # Insert all new assignments
        for assignment in reversed(new_assignments):  # Reverse to maintain order
            init_method.body.insert(insert_index, assignment)

        return tree

    def update_file(self) -> None:
        # Parse the original file
        tree = self.parse_file()

        # Discover all endpoints
        discovered_endpoints = self.discover_all_endpoints()
        print(f"Discovered {len(discovered_endpoints)} endpoints in {self.endpoints_dir}:")
        for module_name, class_name in discovered_endpoints:
            print(f"  - {module_name} -> {class_name}")

        updated_tree = self.update_ast(tree, discovered_endpoints)
        ast.fix_missing_locations(updated_tree)

        updated_code = ast.unparse(updated_tree)

        # Write updated code
        with open(self.driver_file_path, "w", encoding="utf-8") as f:
            f.write(updated_code)

        print(f"File updated: {self.driver_file_path}")


def main():
    typed_driver_parser = ASTEndpointParser(
        endpoints_dir="endpoints", base_driver_class_name="TypedBaseDriverWithEndpoints"
    )
    untyped_driver_parser = ASTEndpointParser(
        endpoints_dir="endpoints_old",
        base_driver_class_name="BaseDriverWithEndpoints",
        modify_module_class_name=lambda x: "Old" + x,
    )

    typed_driver_parser.update_file()
    untyped_driver_parser.update_file()

    run(
        [
            "black",
            "--config",
            "pyproject.toml",
            os.path.join("src", "mattermostautodriver", "driver", "endpoint_base.py"),
        ]
    )


if __name__ == "__main__":
    main()
