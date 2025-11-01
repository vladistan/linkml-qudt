#!/bin/bash

STARTUP_DIR=$(pwd)

set -e # Exit on error

echo "PWD: $PWD"

if [[ "$PWD" == *"/workspaces/"* ]]; then
  echo "Running in VSCode Dev Container"
elif [[ "$PWD" == *"/IdeaProjects/"* ]]; then
  echo "Running in JetBrains IDE"
fi

pre-commit install || true
uv sync
