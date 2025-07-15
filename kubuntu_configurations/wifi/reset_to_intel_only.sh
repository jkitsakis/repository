#!/usr/bin/env bash
# ================================================================
# MEGA SCRIPT: RESET + VERIFY + REBOOT
# Use ONLY built-in Intel Wi-Fi + Bluetooth on Kubuntu
# Removes TP-Link Archer T2UB Nano drivers & resets configs
# ================================================================

echo "⚡ FULL RESET: Using ONLY Intel built-in Wi-Fi and Bluetooth"
echo "🚨 This will REMOVE all custom Wi-Fi/BT profiles, Realtek drivers, firmware, tweaks."
echo "⏳ Starting in 5 seconds... Ctrl+C to cancel."
sleep 5

# -------------------------------
echo "🗑️  Removing saved Wi-Fi/Ethernet profiles..."
sudo rm -v /etc/NetworkManager/system-connections/*

# -------------------------------
echo "⚙️  Restoring default NetworkManager.conf..."
sudo tee /etc/NetworkManager/NetworkManager.conf >/dev/null <<EOF
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true
EOF

# -------------------------------
echo "🧹 Removing Realtek modprobe configs & blacklisting Realtek Wi-Fi modules..."
sudo rm -v /etc/modprobe.d/8821cu.conf 2>/dev/null || true
sudo rm -v /etc/modprobe.d/rtl8821cu.conf 2>/dev/null || true
sudo rm -v /etc/modprobe.d/blacklist-rtw88_8821cu.conf 2>/dev/null || true

# Unload Realtek kernel modules
echo "🔌 Unloading Realtek kernel modules..."
sudo modprobe -r 8821cu rtw88_8821cu rtw88_usb rtw88_core || true

# Blacklist Realtek Wi-Fi drivers
echo "blacklist 8821cu" | sudo tee /etc/modprobe.d/blacklist-8821cu.conf
echo "blacklist rtw88_8821cu" | sudo tee /etc/modprobe.d/blacklist-rtw88_8821cu.conf
echo "blacklist rtw88_usb" | sudo tee -a /etc/modprobe.d/blacklist-rtw88_8821cu.conf
echo "blacklist rtw88_core" | sudo tee -a /etc/modprobe.d/blacklist-rtw88_8821cu.conf

# -------------------------------
echo "🧹 Removing USB autosuspend overrides..."
sudo rm -v /etc/modprobe.d/usbcore-autosuspend.conf 2>/dev/null || true

# -------------------------------
echo "🧹 Removing Intel iwlwifi tweaks (back to default)..."
sudo rm -v /etc/modprobe.d/iwlwifi.conf 2>/dev/null || true

# -------------------------------
echo "🧹 Removing Realtek Bluetooth firmware blobs..."
sudo rm -v /lib/firmware/rtl_bt/rtl8821c_fw.bin 2>/dev/null || true
sudo rm -v /lib/firmware/rtl_bt/rtl8821c_config.bin 2>/dev/null || true

echo "🧹 Removing any Realtek Bluetooth modprobe configs..."
sudo rm -v /etc/modprobe.d/rtl8821cu-bluetooth.conf 2>/dev/null || true

echo "✅ Realtek Bluetooth firmware removed. Only Intel Bluetooth will remain."

# -------------------------------
echo "🔄 Reinstalling default linux-firmware package (Intel Wi-Fi & BT)..."
sudo apt update && sudo apt install --reinstall -y linux-firmware

# -------------------------------
echo "🧵 Rebuilding initramfs to apply all module changes..."
sudo update-initramfs -u

# -------------------------------
echo "🔃 Restarting NetworkManager..."
sudo systemctl restart NetworkManager

# ================================================================
# ✅ VERIFY SECTION
# ================================================================

echo ""
echo "🔍 ✅ VERIFYING Intel-only setup before reboot..."

echo ""
echo "🗂️  [1] Checking loaded Wi-Fi driver modules..."
lsmod | grep iwlwifi && echo "✅ Intel Wi-Fi (iwlwifi) loaded." || echo "❌ Intel Wi-Fi driver NOT loaded!"

echo ""
echo "🗂️  [2] Checking loaded Bluetooth driver modules..."
lsmod | grep btusb && echo "✅ Intel Bluetooth (btusb) loaded." || echo "❌ Intel Bluetooth driver NOT loaded!"

echo ""
echo "🗂️  [3] Checking for Realtek Wi-Fi/Bluetooth modules (should be EMPTY)..."
lsmod | grep -E '88|rtw' && echo "❌ WARNING: Realtek modules STILL loaded!" || echo "✅ No Realtek modules detected."

echo ""
echo "🗂️  [4] Checking connected devices..."
nmcli device status

echo ""
echo "🗂️  [5] Checking active Bluetooth controllers..."
bluetoothctl list

echo ""
echo "🗂️  [6] Checking for leftover Realtek BT firmware files..."
ls /lib/firmware/rtl_bt/ | grep rtl8821c && echo "❌ Realtek BT firmware still exists!" || echo "✅ No Realtek BT firmware blobs detected."

echo ""
echo "✅ Verification complete."
echo "📌 Please PHYSICALLY UNPLUG your TP-Link Archer T2UB Nano USB adapter if still connected."
echo "🔃 Rebooting in 10 seconds..."
sleep 10

sudo reboot
