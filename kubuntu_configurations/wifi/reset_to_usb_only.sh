#!/bin/bash
# reset_to_usb_only.sh
# Disable built-in Intel Wi-Fi, keep USB Realtek active, and reboot.

echo "=== [1] Blacklisting Intel Wi-Fi driver (iwlwifi) ==="
echo "blacklist iwlwifi" | sudo tee /etc/modprobe.d/blacklist-iwlwifi.conf

echo "=== [2] Updating initramfs ==="
sudo update-initramfs -u

echo "=== [3] Unblocking Realtek USB Wi-Fi ==="
sudo rfkill unblock all

echo "=== [4] Installing wireless-tools if missing ==="
sudo apt-get update
sudo apt-get install -y wireless-tools

echo "=== [5] Disabling power saving on Realtek USB Wi-Fi ==="
REALTEK_IFACE=$(iw dev | awk '/Interface/ {print $2}' | grep wl)
sudo iwconfig $REALTEK_IFACE power off

echo "=== [6] Done! Rebooting in 5 seconds ==="
sleep 5
sudo reboot
