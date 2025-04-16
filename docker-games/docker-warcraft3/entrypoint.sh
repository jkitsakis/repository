#!/bin/bash

set -e

export WINEPREFIX=/home/gamer/.wine
export DISPLAY=${DISPLAY:-:0}
export PULSE_SERVER=unix:/tmp/pulseaudio.socket

mkdir -p /home/gamer/game/war3
cd /home/gamer/game

# Extract RAR to writeable path
if [ ! -d "war3/Warcraft.III.Complete.Edition.MULTi6" ]; then
    echo "Extracting Warcraft3.rar..."
    unrar x -o+ Warcraft3.rar war3/
fi

# Find and mount ISO
ISO_PATH=$(find /home/gamer/game/war3 -iname "*.iso" | head -n 1)

if [ -n "$ISO_PATH" ]; then
    echo "Mounting ISO..."
    mkdir -p /mnt/warcraft
    fusermount -u /mnt/warcraft 2>/dev/null || true
    fuseiso "$ISO_PATH" /mnt/warcraft
    cd /mnt/warcraft
    echo "Running game installer..."
    wine Setup.exe
    fusermount -u /mnt/warcraft
fi

# Try launching game
cd "$HOME/.wine/drive_c/Program Files/Warcraft III/" 2>/dev/null || \
cd "$HOME/.wine/drive_c/Program Files (x86)/Warcraft III/" 2>/dev/null || \
cd "$HOME/.wine/drive_c/" 2>/dev/null

echo "Launching Warcraft III..."
wine Warcraft\ III.exe || echo "Game executable not found."
