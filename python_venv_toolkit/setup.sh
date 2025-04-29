#!/bin/bash

set -e

function choose_python() {
    echo "Searching for installed Python versions..."
    mapfile -t pythons < <(compgen -c python | sort -u | grep -E '^python[0-9\.]*$' | xargs -I{} which {} 2>/dev/null | grep -v "not found" | sort -u)

    if [ ${#pythons[@]} -eq 0 ]; then
        echo "No Python versions found."
        return
    fi

    echo "Available Python versions:"
    for i in "${!pythons[@]}"; do
        echo "$((i+1)). ${pythons[$i]}"
    done

    read -rp "Choose a Python version: " py_choice
    selected_python="${pythons[$((py_choice-1))]}"

    if [ ! -x "$selected_python" ]; then
        echo "Invalid selection."
        return
    fi

    echo "Creating virtual environment using: $selected_python..."
    "$selected_python" -m venv .venv
    echo "Virtual environment created in .venv"
}

function export_requirements() {
    if [ ! -d ".venv" ]; then
        echo ".venv not found. Run option 1 first."
        return
    fi

    source .venv/bin/activate

    if ! pip show pipreqs > /dev/null 2>&1; then
        echo "Installing pipreqs..."
        pip install pipreqs
    fi

    echo "Generating requirements.txt..."
    pipreqs . --force --savepath=requirements.txt --use-local --no-pin

    echo "requirements.txt created (no version numbers)."
}

function install_requirements() {
    if [ ! -d ".venv" ]; then
        echo ".venv not found. Run option 1 first."
        return
    fi

    if [ ! -f "requirements.txt" ]; then
        echo "requirements.txt not found. Run option 2 first."
        return
    fi

    source .venv/bin/activate
    echo "Installing packages from requirements.txt..."
    pip install -r requirements.txt
    echo "All packages installed."
}

function main_menu() {
    while true; do
        echo
        echo "1. Choose Python and create .venv"
        echo "2. Export requirements.txt"
        echo "3. Install from requirements.txt"
        echo "4. Exit"
        read -rp "Enter your choice: " choice

        case "$choice" in
            1) choose_python ;;
            2) export_requirements ;;
            3) install_requirements ;;
            4) break ;;
            *) echo "Invalid choice." ;;
        esac
    done
}

main_menu
