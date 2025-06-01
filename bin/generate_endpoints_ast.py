import ast
import json
from collections import namedtuple
from subprocess import run

from inflection import underscore, camelize
from keyword import iskeyword

# Notes about parsing openapi file
#
# Attributes with special significance.
# All these attributes are part of the "paths" key which contains:
# - url_key: first key in the "paths" dictionary is the endpoint URL (e.g. "/users/login")
# - http_type: first key in the "url_key" that identifies the type of HTTP request that can be handled by this endpoint
#   - more on HTTP requests below, including specific arguments for each type
# - tags: the name of the module/file where the function should be stored.
#   - May include one ore more names in which case the function should be duplicated in more than one module
#   - May contain spaces that should be replaced with underscores
# - operation_id: CamelCase identifier used to give name to the API function call (e.g. CreateBot -> create_bot)
#   - Should also be included in the docstring as a URL linking to the original api (e.g. api.mattermost.com/#operation/CreateBot)
# - summary: description of the function that should be included in the docstring
# - parameters
#   - name: the name of the parameter that should be used as-is as a key in GET or POST attributes
#   - description: to be extracted into the docstring
#   - in: the "in" attribute contains either "path" or "query" which:
#     - "query": parameters that should be included as request attributes
#     - "path": parameters that should be included in the URL and string formatted
#   - schema.type: type annotation of parameter (for docstring)
#
# Type of request: Get
#   - Includes only query and path attributes.
#     - Query attributes should be passed as a JSON formatted
#     - Path attributes should be included in the URL and should be arguments to the function and formatted to the URL
# Type of request: Post / Put / Delete
#   - Can include a "requestBody" of type "application/json", "multipart/form-data" or "application/x-www-form-urlencoded"
#     - if "application/json" the options= attribute should be used. It will be sent as JSON
#     - if "application/x-www-form-urlencoded" the data= attribute should be used and a dictionary passed. It will be sent as URL encoded arguments
#     - if "multipart/form-data" the files= attribute should be used but additional arguments may also be passed via options=
#     - "description" should be kept and added to the function docstring as description of the attribute
#     - When including "required: true"
#       - schema.required is sometimes present to indicate properties that should be present in the payload
#       - schema.properties should be extracted and formatted into the docstring
#         - property_name: key in properties dictionary
#         - description: possible description of the attribute
#         - type: type annotation
#         - format: "binary" for file uploads, "int64" for some numeric fields
#     - When attribute isn't required the argument should default to None in the function signature (e.g. params=None)
#
# required = for parameters, there's often a "required: true" value,
#            for properties the field would be present in the "required" array
# type = "string", "integer", "boolean" and in some payloads, "array" and "object"
# default = a default value, usually an integer
# format = "binary" for upload fields, "int64" for some numeric fields
Parameter = namedtuple(
    "Parameter",
    ["name", "description", "required", "type", "default", "format", "schema"],
)


ast_template = """
from ._base import Base
from typing import Any, BinaryIO

__all__ = ["{classname}"]
"""

known_double_arguments = (
    ("update_user_status", "user_id"),
    ("add_team_member", "team_id"),
)


def load_json(filepath="mattermost/api/openapi.json"):
    with open(filepath) as fh:
        return json.loads(fh.read())


def get_parameters(params, key):
    output = {
        "description": "",
        "parameters": [],
        "required": False,
        "schema": None,
    }

    for param in params:
        if param["in"] == key:
            output["parameters"].append(
                Parameter(
                    param["name"],
                    param.get("description", ""),
                    param.get("required", False),
                    param["schema"]["type"],
                    param["schema"].get("default", None),
                    param["schema"].get("format", None),
                    param["schema"],
                )
            )

    return output


def get_properties(schema):
    props = schema.get("properties", {})
    required = schema.get("required", [])

    return [
        Parameter(
            prop,
            values.get("description", ""),
            prop in required,
            values.get("type", None),
            values.get("default", None),
            values.get("format", None),
            values,
        )
        for prop, values in props.items()
    ]


def get_descriptions(params):
    if not params:
        return ""

    # Padding to align with docstring
    doc_pad = "        "

    def fix_docstr(doc):
        return (
            doc.replace("\n", f"\n{doc_pad}")  # Indentation
            .replace("`", "``")  # Convert monospace
            .replace("__", "*")  # Convert emphasis
        )

    return (
        "\n\n" + "\n".join([f"{doc_pad}{par.name}: {fix_docstr(par.description)}" for par in params]) + f"\n{doc_pad}"
    )


def parse_req_body(req_body_type, schema):
    if req_body_type in ("application/json", "multipart/form-data"):
        return get_properties(schema)
    elif req_body_type == "application/x-www-form-urlencoded":
        return []
    else:
        raise NotImplementedError(f"request body type {req_body_type} is not supported")


def get_request_body_type(body):
    if not body:
        return None

    assert len(body["content"]) == 1

    return next(iter(body["content"]))


def get_requestbody_parameters(body, request_type):
    # requestBody can have 3 types "application/json", "multipart/form-data" or "application/x-www-form-urlencoded"
    # - if "application/json" the options= attribute should be used. It will be sent as JSON
    # - if "application/x-www-form-urlencoded" the data= attribute should be used and a dictionary passed. It will be sent as URL encoded arguments
    # - if "multipart/form-data" the files= attribute should be used but additional arguments may also be passed via options=
    # - "description" should be kept and added to the function docstring as description of the attribute
    # - When including "required: true"
    #   - schema.required is sometimes present to indicate properties that should be present in the payload
    #   - schema.properties should be extracted and formatted into the docstring
    #     - property_name: key in properties dictionary
    #     - description: possible description of the attribute
    #     - type: type annotation
    #     - format: "binary" for file uploads, "int64" for some numeric fields
    # - When attribute isn't required the argument should default to None in the function signature (e.g. params=None)

    if not body:
        return {}

    req_body_type = get_request_body_type(body)

    parameters = parse_req_body(req_body_type, body["content"][req_body_type]["schema"])

    binary = [param for param in parameters if param.format == "binary"]

    return {
        "description": body.get("description", ""),
        "parameters": parameters,
        "schema": body["content"][req_body_type]["schema"],
        "required": body.get("required", False),
        "binary": binary,
    }


def get_locations(tags):
    # Locations = which module the function call should be added to
    # NOTE that some identical function calls are present in more than one module/tag
    return [x.replace(" ", "_") for x in tags]


def get_payload_params_or_properties(data, request_type):
    if request_type == "get":
        return get_parameters(data.get("parameters", []), "query")
    else:
        req_body = data.get("requestBody", {})
        return get_requestbody_parameters(req_body, request_type)


def get_link_to_api_docs(tag, operation):
    return (
        f"\n        `Read in Mattermost API docs ({tag} - {operation}) "
        f"<https://api.mattermost.com/#tag/{tag}/operation/{operation}>`_\n\n"
    )


def json_to_ast(api):
    blocks = {}

    for endpoint in api["paths"]:
        for request_type, rdata in api["paths"][endpoint].items():
            try:
                locations = get_locations(rdata["tags"])
            except KeyError:
                print(
                    f"Endpoint {endpoint} for requests of type {request_type} is missing a 'tags' attribute. "
                    "This should be reported upstream. Skipped for now."
                )
                continue

            try:
                operation_id = rdata["operationId"]
            except KeyError:
                # We can't add API entries that don't have a function name
                raise ValueError(f">>> Couldn't create method for {endpoint} due to missing 'operationId'")

            # Function name = underscore conversion of operation_id CamelCase
            function_name = underscore(operation_id)

            # In GET requests we have *query* parameters stored in the parameters object
            # For other types of request we have *properties* in the requestBody
            payload_params = get_payload_params_or_properties(rdata, request_type)

            url_parameters = get_parameters(rdata.get("parameters", {}), "path")

            docstring = rdata["summary"] + get_descriptions(
                url_parameters.get("parameters", []) + payload_params.get("parameters", [])
            )

            req_body = rdata.get("requestBody", {})
            req_body_type = get_request_body_type(req_body)

            # For every HTTP action there's a corresponding variable that should be used
            operations = {
                "delete": "params",
                "get": "params",
                "patch": "options",
                "post": "options",
                "put": "options",
            }

            def_params = prepare_def_keywords(url_parameters, payload_params, operations[request_type], req_body_type, function_name=function_name)
            call_kwargs = prepare_call_keywords(payload_params, operations[request_type], req_body_type)
            data_dicts = prepare_data_dictionaries(payload_params, operations[request_type], req_body_type)

            for loc in locations:
                if loc not in blocks:
                    blocks[loc] = []

                this_docstring = docstring + get_link_to_api_docs(loc, operation_id)

                blocks[loc].append(
                    {
                        "module": loc,
                        "endpoint": endpoint,
                        "request_type": request_type,
                        "function": function_name,
                        "docstring": this_docstring,
                        "call_kwargs": call_kwargs,
                        "def_params": def_params,
                        "data_dicts": data_dicts,
                    }
                )

    return blocks


def generate_type_annotation(schema, required, binary):
    def get_annotation(schema):
        type_mapping = {
            "string": "str",
            "integer": "int",
            "number": "float",
            "boolean": "bool",
            "array": "list",
            "object": "dict",
        }
        if binary:
            return ast.Name(id="BinaryIO", ctx=ast.Load())

        schema_type = schema.get("type", None)

        if schema_type is None:
            return ast.Name(id="Any", ctx=ast.Load())

        if schema_type == "array":
            schema_items = schema.get("items", None)

            if schema_items is None:
                item_type = ast.Name(id="Any", ctx=ast.Load())
            else:
                item_type = get_annotation(schema_items)

            return ast.Subscript(value=ast.Name(id="list", ctx=ast.Load()), slice=item_type, ctx=ast.Load())
        elif schema_type == "object":
            return ast.Subscript(
                value=ast.Name(id="dict", ctx=ast.Load()),
                slice=ast.Tuple(
                    elts=[ast.Name(id="str", ctx=ast.Load()), ast.Name(id="Any", ctx=ast.Load())], ctx=ast.Load()
                ),
                ctx=ast.Load(),
            )

        elif schema_type in type_mapping:
            return ast.Name(id=type_mapping[schema_type], ctx=ast.Load())

        else:
            raise NotImplementedError(f"Type {schema_type} is not supported")

    annotation = get_annotation(schema)

    if not required:
        return ast.BinOp(left=annotation, op=ast.BitOr(), right=ast.Constant(value=None))
    else:
        return annotation


def prepare_call_keywords(payload_params, operation_arg, req_body_type):
    """Convert url parameters to function call arguments

    e.g. func(arg1, arg2=...)
    """

    # Add self to argument list because the function will be part of a class
    kwargs = []

    params = payload_params.get("parameters", [])

    if req_body_type == "multipart/form-data" and payload_params["binary"]:
        kwargs.append(ast.keyword(arg="files", value=ast.Name(f"__files")))

    if req_body_type == "multipart/form-data" and [
        param for param in payload_params["parameters"] if param.format != "binary"
    ]:
        kwargs.append(ast.keyword(arg="data", value=ast.Name(f"__data")))
    elif req_body_type == "application/x-www-form-urlencoded":
        if params:
            kwargs.append(ast.keyword(arg="data", value=ast.Name(f"__data")))
        else:
            kwargs.append(ast.keyword(arg="data", value=ast.Name(f"data")))

    if req_body_type == "application/json":
        if params:
            kwargs.append(ast.keyword(arg=operation_arg, value=ast.Name(f"__{operation_arg}")))
        else:
            kwargs.append(ast.keyword(arg=operation_arg, value=ast.Name(f"{operation_arg}")))

    elif req_body_type is None and payload_params.get("parameters", False):
        kwargs.append(ast.keyword(arg=operation_arg, value=ast.Name(f"__{operation_arg}")))

    return kwargs


def prepare_def_keywords(url_params, payload_params, operation_arg, req_body_type, function_name):
    """Convert url parameters to function arguments

    e.g. def func(arg1, arg2=...):
    """

    def add_param(name, schema, required, binary, default, args, kwargs):
        if iskeyword(name):
            name = name + "_"
        else:
            name = name

        annotation = generate_type_annotation(schema, required, binary)
        args.append(ast.arg(arg=name, annotation=annotation))

        if default is not None:
            kwargs.append(ast.Constant(default))
        elif required:
            kwargs.append(None)
        else:
            kwargs.append(ast.Constant(default))

    args = [ast.arg(arg="self")]
    kwargs = []

    request_params = [*url_params["parameters"]]

    params = payload_params.get("parameters", [])

    if params:
        request_params += params
    elif payload_params and payload_params["schema"] and req_body_type == "application/json":
        request_params.append(
            Parameter(f"{operation_arg}", "", payload_params["required"], None, None, None, payload_params["schema"])
        )
    elif req_body_type == "application/x-www-form-urlencoded":
        request_params.append(
            Parameter(f"data", "", payload_params["required"], None, None, None, payload_params["schema"])
        )

    # Ensure params without default values come first
    request_params.sort(key=lambda param: 0 if param.default is None and param.required else 1)

    existing_params = []
    unique_params = []

    for param in request_params:
        if param.name in existing_params:
            # Some API endpoints repeat arguments in the URL and as part of the payload
            if (function_name, param.name) not in known_double_arguments:
                raise ValueError(f"Saw parameter {param.name} multiple times in endpoint {function_name}")
            continue
        existing_params.append(param.name)
        unique_params.append(param)

    for param in unique_params:
        add_param(param.name, param.schema, param.required, param.format == "binary", param.default, args, kwargs)

    return {"args": args, "defaults": kwargs}


def prepare_data_dictionaries(payload_params, operation_arg, req_body_type):
    def create_dict(name, params):
        def escape_name(name):
            if iskeyword(name):
                return name + "_"
            else:
                return name

        return ast.Assign(
            targets=[ast.Name(id=f"__{name}", ctx=ast.Store())],
            value=ast.Dict(
                keys=[ast.Constant(value=param.name) for param in params],
                values=[ast.Name(id=escape_name(param.name), ctx=ast.Load()) for param in params],
            ),
        )

    dicts = []

    params = payload_params.get("parameters", [])
    binary_params = [param for param in params if param.format == "binary"]
    non_binary_params = [param for param in params if param.format != "binary"]

    if binary_params:
        dicts.append(create_dict("files", binary_params))

    if req_body_type == "application/json" or req_body_type is None:
        if non_binary_params:
            dicts.append(create_dict(operation_arg, non_binary_params))
    elif req_body_type == "multipart/form-data":
        if non_binary_params:
            dicts.append(create_dict("data", non_binary_params))
    elif req_body_type == "application/x-www-form-urlencoded":
        if params:
            dicts.append(create_dict("data", params))
    else:
        raise NotImplementedError(f"Request body of type '{req_body_type}' is not implemented.")

    return dicts


def ast_request(request_type, endpoint, call_params):
    args = [ast.parse(('f"' if "{" in endpoint else '"') + endpoint + '"')]

    return ast.Return(
        ast.Call(
            func=ast.Attribute(
                value=ast.Attribute(
                    value=ast.Name(id="self"),
                    attr="client",
                ),
                attr=request_type,
            ),
            args=args,
            keywords=call_params,
        )
    )


def ast_function(method):
    name = method["function"]
    docstring = method["docstring"]
    def_params = method["def_params"]
    call_kwargs = method["call_kwargs"]
    data_dicts = method["data_dicts"]

    body = [
        ast.Expr(value=ast.Constant(value=docstring)),
        *data_dicts,
        ast_request(method["request_type"], method["endpoint"], call_kwargs),
    ]

    return ast.FunctionDef(
        name=name,
        args=ast.arguments(
            **def_params,
            posonlyargs=[],
            kwonlyargs=[],
        ),
        body=body,
        decorator_list=[],
        lineno=None,
    )


def make_ast(methods, module):
    base = ast.parse(ast_template.format(classname=camelize(module)))
    funcs = [ast_function(method) for method in methods[module]]
    base.body.append(
        ast.ClassDef(
            camelize(module),
            bases=[ast.Name("Base")],
            body=funcs,
            decorator_list=[],
            keywords=[],
        )
    )

    return base


def main():
    api = load_json()
    methods = json_to_ast(api)

    filenames = []

    for module in methods:
        code = make_ast(methods, module)
        filename = f"src/mattermostautodriver/endpoints/{module.lower()}.py"

        with open(filename, "w") as fh:
            ast.fix_missing_locations(code)
            fh.write(ast.unparse(code))

        filenames.append(filename)

    run(["black", "--config", "pyproject.toml", *filenames])


if __name__ == "__main__":
    main()
