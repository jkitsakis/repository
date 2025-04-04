#!/bin/bash

BASEDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$BASEDIR" || exit 1

PYTHON_BIN="python3.12"
APP_FILE="main.py"
VENV_DIR=".venv"
REQ_FILE="requirements.txt"

pause_on_error() {
  echo ""
  echo "⚠️  An error occurred. Press Enter to continue..."
  read -r
}

create_venv() {
  echo "Cleaning old virtual environment..."
  rm -rf "$VENV_DIR" || pause_on_error
  echo "Creating new virtual environment..."
  "$PYTHON_BIN" -m venv "$VENV_DIR" || pause_on_error
  source "$VENV_DIR/bin/activate"
  pip install --upgrade pip setuptools wheel || pause_on_error
  if [ -f "$REQ_FILE" ]; then
    pip install -r "$REQ_FILE" || pause_on_error
  fi
  deactivate
  echo "✅ Virtual environment ready."
}

run_app() {
  if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    create_venv
  fi
  echo "Running $APP_FILE..."
  source "$VENV_DIR/bin/activate"
  python "$APP_FILE" || pause_on_error
  deactivate
}

export_requirements() {
  if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/bin/activate"
    echo "Exporting environment to $REQ_FILE..."
    pip freeze > "$REQ_FILE" || pause_on_error
    deactivate
    echo "✅ Requirements exported."
  else
    echo "⚠️ No virtual environment found."
    pause_on_error
  fi
}

# === Interactive Menu ===
while true; do
  echo ""
  echo "===== Planner App Menu ====="
  echo "1) Run Python app"
  echo "2) Export requirements.txt"
  echo "3) Recreate virtual environment"
  echo "4) Exit"
  echo "============================="
  read -rp "Choose an option [1-4]: " choice

  case "$choice" in
    1) run_app ;;
    2) export_requirements ;;
    3) create_venv ;;
    4) echo "Bye!"; break ;;
    *) echo "Invalid option. Try again." ;;
  esac
done

# Final pause before closing if run from a double-clicked Konsole window
echo ""
read -rp "Press Enter to close..."
