import ast
import os

from subprocess import run


class ASTEndpointParser:
    def __init__(
        self, driver_file_path: str = os.path.join("driver", "endpoint_base.py"), endpoints_dir: str = "endpoints"
    ):
        module_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            os.pardir,
            "src",
            "mattermostautodriver",
        )

        self.driver_file_path = os.path.join(module_path, driver_file_path)
        self.endpoints_path = os.path.join(module_path, endpoints_dir)
        self.endpoints_dir = endpoints_dir

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

    def get_existing_endpoint_imports(self, tree: ast.Module) -> set[tuple[str, str]]:
        """
        Find existing endpoint imports in the AST.

        Returns:
            set of tuples (module_name, class_name)
        """
        existing_imports = set()

        for node in tree.body:
            if isinstance(node, ast.ImportFrom):
                if node.module and node.module.startswith(f"{self.endpoints_dir}.") and node.names:

                    module_name = node.module.split(".")[-1]
                    for alias in node.names:
                        class_name = alias.name
                        existing_imports.add((module_name, class_name))

        return existing_imports

    def create_import_node(self, module_name: str, class_name: str) -> ast.ImportFrom:
        return ast.ImportFrom(
            module=f"{self.endpoints_dir}.{module_name}", names=[ast.alias(name=class_name, asname=None)], level=0
        )

    def create_assignment_node(self, module_name: str, class_name: str) -> ast.Assign:
        attr_name = module_name.lower()

        return ast.Assign(
            targets=[ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr=attr_name, ctx=ast.Store())],
            value=ast.Call(
                func=ast.Name(id=class_name, ctx=ast.Load()),
                args=[ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr="client", ctx=ast.Load())],
                keywords=[],
            ),
        )

    def find_base_driver_with_endpoints_class(self, tree: ast.Module) -> ast.ClassDef:
        """Find the BaseDriverWithEndpoints class in the AST."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "BaseDriverWithEndpoints":
                return node
        raise ValueError("BaseDriverWithEndpoints class not found in the file")

    def find_init_method(self, class_node: ast.ClassDef) -> ast.FunctionDef:
        """Find the __init__ method in a class node."""
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == "__init__":
                return node
        raise ValueError("__init__ method not found in BaseDriverWithEndpoints class")

    def get_existing_endpoint_assignments(self, init_method: ast.FunctionDef) -> set[str]:
        """Get existing endpoint assignments from the __init__ method."""
        existing_assignments = set()

        for node in init_method.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if (
                        isinstance(target, ast.Attribute)
                        and isinstance(target.value, ast.Name)
                        and target.value.id == "self"
                    ):
                        # Check if this looks like an endpoint assignment
                        if (
                            isinstance(node.value, ast.Call)
                            and isinstance(node.value.func, ast.Name)
                            and len(node.value.args) == 1
                            and isinstance(node.value.args[0], ast.Attribute)
                        ):
                            existing_assignments.add(target.attr)

        return existing_assignments

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
        Update the AST with new endpoint imports and assignments.

        Args:
            tree: The original AST
            discovered_endpoints: list of (module_name, class_name) tuples

        Returns:
            Updated AST
        """
        # Get existing imports
        existing_imports = self.get_existing_endpoint_imports(tree)

        # Find imports to add
        new_imports = []
        for module_name, class_name in discovered_endpoints:
            if (module_name, class_name) not in existing_imports:
                new_imports.append(self.create_import_node(module_name, class_name))

        # Add new imports after existing imports but before class definitions
        insert_index = 0
        for i, node in enumerate(tree.body):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                insert_index = i + 1
            elif isinstance(node, ast.ClassDef):
                break

        # Insert new imports
        for import_node in reversed(new_imports):  # Reverse to maintain order
            tree.body.insert(insert_index, import_node)

        # Update the BaseDriverWithEndpoints class
        class_node = self.find_base_driver_with_endpoints_class(tree)
        init_method = self.find_init_method(class_node)

        # Get existing endpoint assignments
        existing_assignments = self.get_existing_endpoint_assignments(init_method)

        # Find where to insert new assignments (after super().__init__ call)
        insert_index = self.find_super_call_index(init_method)

        # Create new assignment nodes
        new_assignments = []
        for module_name, class_name in discovered_endpoints:
            attr_name = module_name.lower()
            if attr_name not in existing_assignments:
                new_assignments.append(self.create_assignment_node(module_name, class_name))

        # Insert new assignments
        for assignment in reversed(new_assignments):  # Reverse to maintain order
            init_method.body.insert(insert_index, assignment)

        return tree

    def update_file(self) -> None:
        # Parse the original file
        tree = self.parse_file()

        # Discover all endpoints
        discovered_endpoints = self.discover_all_endpoints()
        print(f"Discovered {len(discovered_endpoints)} endpoints:")
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
    parser = ASTEndpointParser()
    parser.update_file()

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
