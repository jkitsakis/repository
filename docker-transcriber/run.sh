#!/bin/bash

DEMO_NAME="Transcriber"
APP_HOME="$(pwd)/app"
PYTHON_ENV="$APP_HOME/.venv"
PYTHON_BIN="$PYTHON_ENV/bin"

export PATH="$PYTHON_BIN:$PATH"

function show_menu() {
  clear
  echo
  echo "       ---------------------------"
  echo "             Main Menu"
  echo "       ---------------------------"
  echo "  1. Run in Docker Container $DEMO_NAME"
  echo "  2. Run locally $DEMO_NAME"
  echo "  3. Export requirements.txt $DEMO_NAME"
  echo "  4. Install packages from requirements.txt $DEMO_NAME"
  echo "  5. Uninstall All packages $DEMO_NAME"
  echo "  0. Exit"
  echo
}

function run_docker() {
  echo "Starting..."
  podman exec -it transcriber-container python /app/transcriber.py --model_size large --hftoken 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 --language en
  read -p "Press Enter to continue..."
}

function run_local() {
  clear
  cd "$APP_HOME" || exit
  "$PYTHON_BIN/python" main.py
  echo "Planner script finished."
  read -p "Press Enter to continue..."
}

function export_requirements() {
  source "$PYTHON_BIN/activate"
  cd "$APP_HOME" || exit
  pip freeze > requirements.txt
  mv requirements.txt "$APP_HOME"
  read -p "Press Enter to continue..."
}

function update_packages() {
  source "$PYTHON_BIN/activate"
  cd "$APP_HOME" || exit
  python -m pip install --upgrade pip || echo "❌ Failed to upgrade pip!"
  pip install --upgrade --no-cache-dir -r requirements.txt
  read -p "Press Enter to continue..."
}

function uninstall_all() {
  source "$PYTHON_BIN/activate"
  cd "$APP_HOME" || exit
  pip freeze | xargs pip uninstall -y
  read -p "Press Enter to continue..."
}

while true; do
  show_menu
  read -p "Type option: " opt
  case "$opt" in
    0) clear; echo "Exiting..."; break ;;
    1) run_docker ;;
    2) run_local ;;
    3) export_requirements ;;
    4) update_packages ;;
    5) uninstall_all ;;
    *) echo "Invalid option."; read -p "Press Enter to continue..." ;;
  esac
done
