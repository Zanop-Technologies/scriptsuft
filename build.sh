#!/bin/sh
# Build script for Scriptsuft
# TODO: Implement the parser in assembly (see scriptsuft_basic.asm)
# TODO: Implement the interactive console in Python (console.py)

set -e
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
DIST="$ROOT_DIR/dist"
mkdir -p "$DIST"

# Create a placeholder runtime bundle
OUT="$DIST/scriptsuft.txt"
echo "Scriptsuft placeholder runtime" > "$OUT"

echo "-- scriptsuft_basic.asm (source) --" >> "$OUT"
cat "$ROOT_DIR/scriptsuft_basic.asm" >> "$OUT" || true

echo "" >> "$OUT"
echo "TODO: Parser is not implemented. Intended: implement parser in ASM. See scriptsuft_basic.asm." >> "$OUT"
echo "TODO: Console is not implemented. Intended: implement interactive console in Python (console.py)." >> "$OUT"

chmod +x "$OUT"

echo "Built: $OUT"
exit 0
