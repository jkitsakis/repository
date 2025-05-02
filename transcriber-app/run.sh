#!/bin/bash

VENV_PATH="$HOME/workspace/transcriber-app/.venv"

function create_venv() {
    echo "📦 Creating Python virtual environment at $VENV_PATH ..."
    python3 -m venv "$VENV_PATH"
    echo "✅ Virtual environment created."
}

function activate_venv() {
    source "$VENV_PATH/bin/activate"
}

function install_requirements() {
    if [ ! -d "$VENV_PATH" ]; then
        echo "⚙️  No .venv found. Creating .venv first..."
        create_venv
    fi
    echo "📜 Installing requirements from requirements.txt ..."
    activate_venv
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "✅ Requirements installed."
}

function run_transcriber() {
    if [ ! -d "$VENV_PATH" ]; then
        echo "⚙️  No .venv found. Creating .venv first..."
        create_venv
        install_requirements
    fi
    echo "🎬 Running Transcriber App..."
    activate_venv
    . .venv/bin/activate
    python run_transcription.py
}

function reset_venv() {
    echo "⚠️  Deleting existing virtual environment at $VENV_PATH ..."
    rm -rf "$VENV_PATH"
    echo "✅ .venv has been reset."
}

function copy_to_windows_folder(){
	rsync -av --exclude='.venv' --exclude='whisper.cpp' --exclude='input' --exclude='audio' --exclude='output' --exclude='models' ./ /mnt/c/Workspace/My-Applications/GitHub/repository/transcriber-app/
}


while true; do
    echo ""
    echo "=============================="
    echo "      TRANSCRIBER MENU        "
    echo "=============================="
    echo "1. ▶️  Run Transcriber App"
    echo "2. 📜 Install requirements.txt"
    echo "3. 🛠 Create and Activate .venv"
    echo "4. ♻️  Reset .venv (Delete and Recreate)"
	echo "5. ▶️  Sync from WSL → to Windows folder"
    echo "6. ❌ Exit"
    echo "=============================="
    read -p "Select an option [1-5]: " choice

    case $choice in
        1)
            run_transcriber
            ;;
        2)
            install_requirements
            ;;
        3)
            create_venv
            activate_venv
            ;;
        4)
            reset_venv
            ;;
		5)
			copy_to_windows_folder
			;;
        6)
            echo "👋 Goodbye!"
            exit 0
            ;;
        *)
            echo "❗ Invalid choice. Please select 1, 2, 3, 4, or 5."
            ;;
    esac
done
