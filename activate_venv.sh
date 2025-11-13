#!/bin/bash
# Script to activate the virtual environment for pyglowmarkt project
# Usage: source ./activate_venv.sh

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_PATH="$SCRIPT_DIR/venv"

if [ ! -d "$VENV_PATH" ]; then
    echo "Virtual environment not found at $VENV_PATH"
    echo "Creating virtual environment..."
    python -m venv "$VENV_PATH"
    echo "Installing dependencies..."
    "$VENV_PATH/bin/pip" install -e "$SCRIPT_DIR"
fi

echo "Activating virtual environment..."
source "$VENV_PATH/bin/activate"
echo "Virtual environment activated: $(which python)"
