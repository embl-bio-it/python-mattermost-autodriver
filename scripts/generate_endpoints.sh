#!/usr/bin/env bash

GREEN="\e[1;32m"
RESET="\e[0m"

color() {
    echo -e "${GREEN}$1${RESET}"
}

set -eu

STORE_DIR="mattermostautodriver"

DEST="endpoints"
# Remove all generated modules but keep _base.py which is a regular
# source file (defines Base and the FileType upload annotations)
find src/$STORE_DIR/$DEST -name '*.py' ! -name '_base.py' -delete
touch src/$STORE_DIR/$DEST/__init__.py

color "Generating new API endpoints"
python bin/generate_endpoints_ast.py

color "Updating driver"
python bin/generate_driver_ast.py

color "Updating documentation for new endpoints"
# Executing in a subshell so we don't have to worry about a failing chdir
( cd docs && python update_endpoints.py )
