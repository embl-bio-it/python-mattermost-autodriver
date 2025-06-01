#!/usr/bin/env bash

GREEN="\e[1;32m"
RESET="\e[0m"

color() {
    echo -e "${GREEN}$1${RESET}"
}

set -eu

STORE_DIR="mattermostautodriver"

for DEST in "endpoints" "endpoints_old"; do
    rm -f src/$STORE_DIR/$DEST/*.py
    touch src/$STORE_DIR/$DEST/__init__.py

    cat << EOF > src/$STORE_DIR/$DEST/_base.py
class Base:
    def __init__(self, client):
        self.client = client
EOF
done

color "Generating deprecated-style endpoints"
python bin/generate_endpoints_ast_deprecated.py

color "Generating new API endpoints"
python bin/generate_endpoints_ast.py

color "Updating documentation for new endpoints"
# Executing in a subshell so we don't have to worry about a failing chdir
( cd docs && python update_endpoints.py )
