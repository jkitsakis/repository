
#!/bin/bash

DEMO_NAME="Assistant"
APP_HOME="$(pwd)/app"
PYTHON_ENV="$(pwd)/.venv"
PYTHON_BIN="$PYTHON_ENV/bin"
PATH="$PYTHON_BIN:$PATH"

activate_env() {
    if [ -f "$PYTHON_BIN/activate" ]; then
        source "$PYTHON_BIN/activate"
    else
        echo "❌ Virtual environment not found!"
        exit 1
    fi
}

run_assistant() {
    clear
    cd "$APP_HOME" || exit
    python3 "$APP_HOME/start_assistant.py" --apikey="your-openai-key-here" --defaultlang="Greek" --modelfolder="$APP_HOME/model" --soundsfolder="$APP_HOME/sounds"
    echo "$DEMO_NAME script finished."
    read -p "Press Enter to continue..."
}

export_requirements() {
    activate_env
    cd "$APP_HOME" || exit
    pip freeze > requirements.txt
    mv requirements.txt "$APP_HOME/"
    echo "✅ Requirements exported."
    read -p "Press Enter to continue..."
}

upgrade_packages() {
    activate_env
    cd "$APP_HOME" || exit
    python3 -m pip install --upgrade pip || echo "❌ Failed to upgrade pip!"
    pip install --upgrade --no-cache-dir -r requirements.txt
    echo "✅ Packages upgraded."
    read -p "Press Enter to continue..."
}

uninstall_all() {
    activate_env
    cd "$APP_HOME" || exit
    pip freeze | xargs pip uninstall -y
    echo "✅ All packages uninstalled."
    read -p "Press Enter to continue..."
}

open_cmd() {
    activate_env
    if command -v konsole &> /dev/null; then
        konsole --workdir "$APP_HOME" &
    elif command -v gnome-terminal &> /dev/null; then
        gnome-terminal --working-directory="$APP_HOME" &
    else
        echo "❌ No terminal emulator found!"
    fi
    read -p "Press Enter to continue..."
}

main_menu() {
    while true; do
        clear
        echo "---------------------------"
        echo "         Main Menu"
        echo "---------------------------"
        echo "1. Run $DEMO_NAME"
        echo "2. Export requirements.txt"
        echo "3. Upgrade packages"
        echo "4. Uninstall all packages"
        echo "cmd. Open terminal with environment"
        echo "0. Exit"
        echo
        read -p "Type option: " opt

        case $opt in
            1) run_assistant ;;
            2) export_requirements ;;
            3) upgrade_packages ;;
            4) uninstall_all ;;
            cmd) open_cmd ;;
            0) deactivate; clear; exit 0 ;;
            *) echo "❌ Invalid option!"; sleep 2 ;;
        esac
    done
}

main_menu
