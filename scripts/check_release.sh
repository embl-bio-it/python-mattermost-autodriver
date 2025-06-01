#!/usr/bin/env bash

MM="mattermost"
PYPI_PACKAGE="mattermostautodriver"

if ! TAGS_JSON="$(curl -s -f https://api.github.com/repos/${MM}/${MM}/tags)"; then
  echo "GitHub API call failed"
  exit 1
fi

# Extract and sort version tags
LATEST_TAG="$(echo "$TAGS_JSON" | jq -r '.[].name' | grep '^v' | grep -v -- '-rc' | sort -V | tail -n 1)"

if [ -z "$LATEST_TAG" ]; then
  echo "No version tags found"
  exit 1
fi

LATEST_TAG="v10.8.2"
echo "Latest Mattermost Server GitHub tag: $LATEST_TAG"

# Check if the version exists on PyPI - strip 'v' as Mattermost has it in the tag but we don't on PyPI
VERSION="${LATEST_TAG#v}"

if ! PYPI_VERSIONS=$(curl -s -f https://pypi.org/pypi/$PYPI_PACKAGE/json); then
  echo "Failed to retrieve versions from PyPI"
  exit 1
fi

if echo "$PYPI_VERSIONS" | jq -e --arg ver "$VERSION" '.releases[$ver]' > /dev/null; then
  echo "MattermostAutoDriver version $VERSION exists on PyPI"
  exit 1
else
  echo "MattermostAutoDriver version $VERSION not found on PyPI"
  exit 0
fi
