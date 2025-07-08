#!/bin/bash

REPO_URL="https://github.com/brektrou/rtl8821CU.git"
REPO_DIR="$HOME/rtl8821CU"

BLACKLIST_CONF="/etc/modprobe.d/blacklist-intel.conf"

function install_driver() {
  echo "==> Installing rtl8821CU Wi-Fi driver..."

  if [ ! -d "$REPO_DIR" ]; then
    git clone $REPO_URL "$REPO_DIR" || { echo "Git clone failed"; exit 1; }
  else
    echo "Repo already cloned. Pulling latest changes..."
    cd "$REPO_DIR" && git pull || { echo "Git pull failed"; exit 1; }
  fi

  cd "$REPO_DIR" || exit 1

  echo "Compiling driver..."
  make clean
  make || { echo "Make failed"; exit 1; }
  sudo make install || { echo "Make install failed"; exit 1; }

  echo "Loading driver module..."
  sudo modprobe -r 8821cu 2>/dev/null
  sudo modprobe 8821cu || { echo "modprobe failed"; exit 1; }

  echo "Driver installed and loaded."
}

function blacklist_intel() {
  echo "==> Blacklisting Intel Wi-Fi and Bluetooth modules..."

  sudo tee $BLACKLIST_CONF > /dev/null <<EOF
blacklist iwlwifi
blacklist iwlmvm
blacklist btusb
EOF

  echo "Updating initramfs..."
  sudo update-initramfs -u

  echo "Intel drivers blacklisted."
}

function reload_bluetooth() {
  echo "==> Reloading Bluetooth USB module..."

  sudo modprobe -r btusb 2>/dev/null
  sudo modprobe btusb || echo "Warning: btusb modprobe failed. Check firmware."

  echo "Bluetooth module reloaded."
}

function verify_status() {
  echo "==> Verifying Wi-Fi and Bluetooth status..."

  echo "--- USB device detection ---"
  lsusb | grep -i "8821cu\|Realtek"

  echo "--- Kernel modules loaded ---"
  lsmod | grep -E "8821cu|iwlwifi|btusb"

  echo "--- Network interfaces ---"
  ip link show | grep -E "wlan|wl"

  echo "--- Bluetooth controllers ---"
  bluetoothctl list

  echo "Verification complete."
}

function revert_changes() {
  echo "==> Reverting blacklists and uninstalling rtl8821CU driver..."

  # Remove blacklist file
  if [ -f "$BLACKLIST_CONF" ]; then
    sudo rm -f "$BLACKLIST_CONF"
    echo "Removed blacklist file."
  else
    echo "Blacklist file not found."
  fi

  echo "Updating initramfs..."
  sudo update-initramfs -u

  # Remove installed driver
  if [ -d "$REPO_DIR" ]; then
    cd "$REPO_DIR" || exit 1
    sudo make uninstall || echo "Uninstall failed or not supported."
    cd -
    # Optionally remove repo
    # rm -rf "$REPO_DIR"
  else
    echo "Driver repo not found. Skipping uninstall."
  fi

  # Unload rtl8821cu module
  sudo modprobe -r 8821cu 2>/dev/null

  echo "Reverted changes. Please reboot your system."
}

function show_menu() {
  echo "==============================="
  echo " Archer T2UB Nano Setup Script - run with sudo ./setup_archer_t2ub_menu.sh"
  echo "==============================="
  echo "1) Install driver and disable Intel adapters"
  echo "2) Verify Wi-Fi and Bluetooth status"
  echo "3) Revert changes (reenable Intel, uninstall driver)"
  echo "4) Exit"
  echo -n "Select an option [1-4]: "
}

if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root (sudo)."
  exit 1
fi

while true; do
  show_menu
  read -r choice
  case $choice in
    1)
      install_driver
      blacklist_intel
      reload_bluetooth
      echo "Setup complete. Please reboot your system."
      ;;
    2)
      verify_status
      ;;
    3)
      revert_changes
      ;;
    4)
      echo "Exiting."
      exit 0
      ;;
    *)
      echo "Invalid option. Please select 1, 2, 3 or 4."
      ;;
  esac
  echo
done
