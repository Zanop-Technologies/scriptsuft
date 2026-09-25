#!/bin/sh
# Build script for Scriptsuft

set -eu
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

python3 "$ROOT_DIR/scriptsuft.py" build
