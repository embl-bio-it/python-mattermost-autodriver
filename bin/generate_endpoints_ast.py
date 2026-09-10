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
# placement = where the value is sent on the wire: "url" for path
#             interpolation, otherwise the client keyword whose dictionary
#             carries it ("params", "options", "data" or "files")
# passthrough = the value is passed to the client keyword directly instead of
#               being wrapped in a dictionary (catch-all request bodies)
Parameter = namedtuple(
    "Parameter",
    ["name", "description", "required", "type", "default", "format", "schema", "placement", "passthrough"],
    defaults=(False,),
)

# A function argument: one or more same-named parameters merged across all
# the placements the value is sent to (see collect_arguments)
Argument = namedtuple(
    "Argument",
    ["name", "description", "required", "type", "default", "format", "schema", "placements", "passthrough"],
)

# Client keywords whose parameters are collected into dictionaries, in the
# order the dictionaries are built and passed to the client
placement_keywords = ("params", "files", "data", "options")


def escape_name(name):
    # Python keywords cannot be used as argument names
    return name + "_" if iskeyword(name) else name


def placed_arguments(arguments, keyword, passthrough=False):
    return [arg for arg in arguments if keyword in arg.placements and arg.passthrough == passthrough]


ast_template = """
from ._base import Base, FileType
from typing import Any

__all__ = ["{classname}"]
"""

known_double_arguments = (
    ("update_user_status", "user_id"),
    ("add_team_member", "team_id"),
    ("convert_group_message_to_channel", "channel_id"),
    # channel_id may be sent as a multipart form field and/or a query parameter
    ("upload_file", "channel_id"),
)


def load_json(filepath="mattermost/api/openapi.json"):
    with open(filepath) as fh:
        return json.loads(fh.read())


def get_parameters(params, key, placement):
    return [
        Parameter(
            param["name"],
            param.get("description", ""),
            param.get("required", False),
            param["schema"]["type"],
            param["schema"].get("default", None),
            param["schema"].get("format", None),
            param["schema"],
            placement,
        )
        for param in params
        if param["in"] == key
    ]


def get_properties(schema, placement, binary_placement=None):
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
            binary_placement if binary_placement and values.get("format") == "binary" else placement,
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

    def describe(par):
        description = fix_docstr(par.description)
        # Defaults from the API specification document what the server
        # applies when the parameter is omitted - they are not sent by us
        if par.default is not None and not par.required:
            note = f"Default: ``{par.default!r}`` (applied server-side when omitted)"
            if not description.strip():
                description = note
            elif "\n" in description.strip():
                # Multi-line descriptions get the note as a separate paragraph
                # so it doesn't run into whatever the last line happens to be
                # (often standalone markup like *Minimum server version*: X)
                description = f"{description.rstrip()}\n\n{doc_pad}{note}"
            else:
                description = f"{description.strip()} {note}"
        return f"{doc_pad}{par.name}: {description}"

    return "\n\n" + "\n".join([describe(par) for par in params]) + f"\n{doc_pad}"


def parse_req_body(req_body_type, schema, placement):
    if req_body_type == "application/json":
        return get_properties(schema, placement)
    elif req_body_type == "multipart/form-data":
        # Binary properties are uploaded as files, the rest as form data
        return get_properties(schema, placement, binary_placement="files")
    elif req_body_type == "application/x-www-form-urlencoded":
        return []
    else:
        raise NotImplementedError(f"request body type {req_body_type} is not supported")


def get_request_body_type(body):
    if not body:
        return None

    # Some endpoints offer the same payload under multiple content types
    # (e.g. application/octet-stream *and* multipart/form-data for file uploads).
    # We don't support raw octet-stream bodies, so strip it and keep the form.
    content_types = [ct for ct in body["content"] if ct != "application/octet-stream"]

    if len(content_types) > 1:
        raise ValueError(f"Request body has more than 1 content types after filtering: {content_types}")
    if len(content_types) == 0:
        raise ValueError(f"Request body has no content types after filtering: {body}")

    return content_types[0]


def get_requestbody_parameters(body, placement):
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

    parameters = parse_req_body(req_body_type, body["content"][req_body_type]["schema"], placement)

    return {
        "description": body.get("description", ""),
        "parameters": parameters,
        "schema": body["content"][req_body_type]["schema"],
        "required": body.get("required", False),
    }


def get_locations(tags):
    # Locations = which module the function call should be added to
    # NOTE that some identical function calls are present in more than one module/tag
    return [x.replace(" ", "_") for x in tags]


def collect_arguments(parameters, function_name):
    """Merge same-named parameters into single function arguments

    Some API endpoints take the same value in more than one location (e.g. in
    the URL and repeated in the payload). Such parameters must be explicitly
    listed in known_double_arguments and become a single function argument
    whose value is sent to every placement.
    """
    arguments = {}

    for param in parameters:
        if param.name not in arguments:
            fields = param._asdict()
            fields["placements"] = (fields.pop("placement"),)
            arguments[param.name] = Argument(**fields)
            continue

        if (function_name, param.name) not in known_double_arguments:
            raise ValueError(f"Saw parameter {param.name} multiple times in endpoint {function_name}")

        existing = arguments[param.name]

        # A double argument is one value sent to several placements, which
        # only works if every placement agrees on what that value looks like
        if (existing.type, existing.format) != (param.type, param.format):
            raise ValueError(
                f"Parameter {param.name} in endpoint {function_name} has diverging types across "
                f"placements: {existing.type}/{existing.format} vs {param.type}/{param.format}"
            )

        arguments[param.name] = existing._replace(
            description=existing.description or param.description,
            required=existing.required or param.required,
            placements=existing.placements + (param.placement,),
        )

    return list(arguments.values())


def get_link_to_api_docs(tag, operation):
    return (
        f"\n        `Read in Mattermost API docs ({tag} - {operation}) "
        f"<https://developers.mattermost.com/api-documentation/#/operations/{operation}>`_\n\n"
    )


def json_to_ast(api):
    blocks = {}

    for endpoint in api["paths"]:
        functions_seen = set()
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
                print(
                    f">>> Couldn't create method for {endpoint} due to missing 'operationId'. "
                    "This should be reported upstream. Skipped for now."
                )
                continue

            # Function name = underscore conversion of operation_id CamelCase
            function_name = underscore(operation_id)

            if function_name not in functions_seen:
                functions_seen.add(function_name)
            else:
                raise ValueError(f">>> 'operationId' {operation_id} generated non-unique function {function_name}")

            # For every HTTP action there's a corresponding client keyword
            # carrying its payload. NOTE for delete this means the payload is
            # sent as query parameters rather than as a request body.
            operations = {
                "delete": "params",
                "get": "params",
                "head": "params",
                "patch": "options",
                "post": "options",
                "put": "options",
            }
            operation_arg = operations[request_type]

            req_body_type = get_request_body_type(rdata.get("requestBody", {}))

            url_parameters = get_parameters(rdata.get("parameters", []), "path", "url")

            # Query parameters are sent through params= for every request
            # type; for GET/HEAD requests they are the entire payload
            query_parameters = get_parameters(rdata.get("parameters", []), "query", "params")

            if request_type in ("get", "head"):
                payload = {}
            else:
                payload_placement = (
                    "data"
                    if req_body_type in ("multipart/form-data", "application/x-www-form-urlencoded")
                    else operation_arg
                )
                payload = get_requestbody_parameters(rdata.get("requestBody", {}), payload_placement)

            parameters = url_parameters + payload.get("parameters", [])

            # Request bodies without listed properties become a single
            # catch-all argument passed straight to the client keyword
            if payload and not payload["parameters"]:
                if req_body_type == "application/json" and payload["schema"]:
                    name = operation_arg
                elif req_body_type == "application/x-www-form-urlencoded":
                    name = "data"
                else:
                    name = None

                if name is not None:
                    parameters.append(
                        Parameter(name, "", payload["required"], None, None, None, payload["schema"], name, True)
                    )

            arguments = collect_arguments(parameters + query_parameters, function_name)

            docstring = rdata["summary"] + get_descriptions(
                [argument for argument in arguments if not argument.passthrough]
            )

            def_params = prepare_def_keywords(arguments)
            call_kwargs = prepare_call_keywords(arguments)
            data_dicts = prepare_data_dictionaries(arguments)

            for loc in locations:
                # NOTE tags in the original OpenAPI specification use a combination of
                # CamelCase, "multi word" and under_score styles.
                # To keep things consistent and avoid clashes, we force underscore style
                # This also addesses issues when tags in the OpenAPI specification
                # are inconsistently used in uppercase and lowercase (e.g. LDAP and ldap)
                loc = underscore(loc)
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
            return ast.Name(id="FileType", ctx=ast.Load())

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


def prepare_call_keywords(arguments):
    """Convert arguments to client call keywords

    e.g. self.client.post(url, params=__params, options=__options)
    """

    kwargs = []

    for keyword in placement_keywords:
        placed = placed_arguments(arguments, keyword)
        passthrough = placed_arguments(arguments, keyword, passthrough=True)

        if placed and passthrough:
            # e.g. a DELETE with both a catch-all request body (sent as
            # params=) and query parameters - both target the same keyword
            raise NotImplementedError(
                f"Both individual parameters and a catch-all payload target the client keyword {keyword}"
            )

        if placed:
            kwargs.append(ast.keyword(arg=keyword, value=ast.Name(f"__{keyword}")))

        for argument in passthrough:
            kwargs.append(ast.keyword(arg=keyword, value=ast.Name(argument.name)))

    return kwargs


def prepare_def_keywords(arguments):
    """Convert arguments to a function signature

    e.g. def func(arg1, arg2=...):
    """

    # Add self to argument list because the function will be part of a class
    args = [ast.arg(arg="self")]
    kwargs = []

    # Ensure required arguments come first
    for argument in sorted(arguments, key=lambda argument: 0 if argument.required else 1):
        annotation = generate_type_annotation(argument.schema, argument.required, argument.format == "binary")
        args.append(ast.arg(arg=escape_name(argument.name), annotation=annotation))

        # Defaults from the API specification are deliberately NOT used here:
        # they describe what the server applies when a parameter is omitted.
        # Optional parameters default to None, which the client filters out
        # before sending, so the server-side default always takes effect.
        if argument.required:
            kwargs.append(None)
        else:
            kwargs.append(ast.Constant(None))

    return {"args": args, "defaults": kwargs}


def prepare_data_dictionaries(arguments):
    def create_dict(name, placed):
        return ast.Assign(
            targets=[ast.Name(id=f"__{name}", ctx=ast.Store())],
            value=ast.Dict(
                keys=[ast.Constant(value=argument.name) for argument in placed],
                values=[ast.Name(id=escape_name(argument.name), ctx=ast.Load()) for argument in placed],
            ),
        )

    dicts = []

    for keyword in placement_keywords:
        placed = placed_arguments(arguments, keyword)
        if placed:
            dicts.append(create_dict(keyword, placed))

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
    classname = camelize(module)
    base = ast.parse(ast_template.format(classname=classname))
    funcs = [ast_function(method) for method in methods[module]]
    base.body.append(
        ast.ClassDef(
            classname,
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
        filename = f"src/mattermostautodriver/endpoints/{module}.py"

        with open(filename, "w") as fh:
            ast.fix_missing_locations(code)
            fh.write(ast.unparse(code))

        filenames.append(filename)

    run(["black", "--config", "pyproject.toml", *filenames])


if __name__ == "__main__":
    main()
