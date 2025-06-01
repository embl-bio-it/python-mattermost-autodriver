#!/usr/bin/env bash

set -eu

STORE_DIR="mattermostautodriver"

for DEST in "endpoints" "endpoints_old"; do
    rm -f "src/$STORE_DIR/$DEST/*.py"
    touch "src/$STORE_DIR/$DEST/__init__.py"

    cat << EOF > src/$STORE_DIR/$DEST/_base.py
class Base:
    def __init__(self, client):
        self.client = client
EOF
done

python bin/generate_endpoints_ast_deprecated.py
python bin/generate_endpoints_ast.py
