#!/bin/bash

# Define the source directory for ply and the destination directory for the bundled version
PLY_SRC_DIR=$(dirname $(poetry run python -c "import ply; print(ply.__file__)"))
BUNDLE_DIR="udmfio_bundled"
DEST_LIB_DIR="$BUNDLE_DIR/libs"

# Create the directories if they don't exist
mkdir -p "$BUNDLE_DIR"
mkdir -p "$DEST_LIB_DIR"

# Copy your project files to bundled_version (excluding any virtual environments or other directories you don't want)
rsync -av --exclude=venv/ --exclude=$BUNDLE_DIR/ --exclude=__pycache__/ ./udmfio/ "$BUNDLE_DIR/"

# Copy ply to the libs directory inside bundled_version
cp -r "$PLY_SRC_DIR" "$DEST_LIB_DIR"

# Update the imports in the parser.ply file inside the bundled_version
PARSER_FILE_PATH="$BUNDLE_DIR/parser.py"

# Using sed to perform the replacement
sed -i '' 's/import ply.lex as lex/from .libs.ply import lex/g' "$PARSER_FILE_PATH"
sed -i '' 's/import ply.yacc as yacc/from .libs.ply import yacc/g' "$PARSER_FILE_PATH"

echo "PLY bundled and parser.ply patched successfully in $BUNDLE_DIR!"
