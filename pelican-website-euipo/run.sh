#!/bin/bash

PORT=5050
DEMO_NAME="EUIPO Pelican"
APP_HOME="$(pwd)"
PYTHON_ENV="$APP_HOME/.venv"
PYTHON_BIN="$PYTHON_ENV/bin"
export PYTHONPATH="$APP_HOME"
export PATH="$PYTHON_BIN:$PATH"

function menu() {
    clear
    echo "========================================="
    echo "         $DEMO_NAME - MAIN MENU"
    echo "========================================="
    echo " 1. Build $DEMO_NAME"
    echo " 2. Run $DEMO_NAME"
    echo " 3. Export requirements.txt"
    echo " 4. Update/install packages"
    echo " 5. Uninstall all packages"
    echo " 6. Open shell with virtualenv"
    echo " 0. Exit"
    echo "-----------------------------------------"
    read -p "Type option: " opt

    case "$opt" in
        0) exit_script ;;
        1) build ;;
        2) run ;;
        3) export_reqs ;;
        4) update_packages ;;
        5) uninstall_all ;;
        6) open_shell ;;
        *) menu ;;
    esac
}

function activate_venv() {
    source "$PYTHON_ENV/bin/activate"
}

function uninstall_all() {
    activate_venv
    echo "Uninstalling all packages..."
    pip freeze | xargs pip uninstall -y
    read -p "Press enter to return to menu..."
    menu
}

function open_shell() {
    activate_venv
    echo "Virtual environment shell. Type 'exit' to return."
    bash --rcfile <(echo "PS1='(venv) \w\$ '")
    menu
}

function export_reqs() {
    activate_venv
    echo "Exporting requirements.txt..."
    pip list --not-required --format=freeze | sed 's/==.*//' > requirements.txt
    echo "Saved to: $APP_HOME/requirements.txt"
    read -p "Press enter to return to menu..."
    menu
}

function update_packages() {
    activate_venv
    echo "Updating pip and all packages..."
    python -m pip install --upgrade pip || echo "❌ Failed to upgrade pip"
    pip install --upgrade --no-cache-dir -r "$APP_HOME/requirements.txt"
    read -p "Press enter to return to menu..."
    menu
}

function build() {
    activate_venv
    echo "Building site..."
    rm -rf "$APP_HOME/output"
    pelican content --delete-output
    pelican content -D
    read -p "Press enter to return to menu..."
    menu
}

function run() {
    activate_venv
    echo "Running Pelican with live reload on port $PORT..."
    nohup pelican -lr -p "$PORT" > pelican.log 2>&1 &
    PELICAN_PID=$!
    sleep 2
    xdg-open "http://localhost:$PORT" || x-www-browser "http://localhost:$PORT"
    # Wait for user to finish
    read -rp "Press Enter to stop server and exit..."
    kill "$PELICAN_PID" 2>/dev/null && echo "Pelican stopped."
    sleep 2
    PID=$(lsof -ti tcp:"$PORT")
    kill "$PID"
    menu
}

function exit_script() {
    if [[ -f "$PYTHON_ENV/bin/activate" ]]; then
        activate_venv
        deactivate
    fi
    clear
    pkill -f pelican
    echo "Exiting... 👋"
    exit 0
}

# Start the menu loop
menu
