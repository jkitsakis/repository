#!/bin/bash
#wifi logs : sudo dmesg | grep iwlwifi

echo "=== Intel Wi-Fi Quick Fix Script ==="

# Backup existing config
if [ -f /etc/modprobe.d/iwlwifi.conf ]; then
  sudo cp /etc/modprobe.d/iwlwifi.conf /etc/modprobe.d/iwlwifi.conf.bak
  echo "[+] Existing iwlwifi.conf backed up to iwlwifi.conf.bak"
fi

# Create new config
echo "[+] Writing recommended driver options..."

sudo bash -c 'cat > /etc/modprobe.d/iwlwifi.conf <<EOF
# Intel iwlwifi driver stability tweaks
options iwlwifi swcrypto=1 bt_coex_active=0 11n_disable=1 power_save=0
EOF'

echo "[+] iwlwifi.conf written:"
cat /etc/modprobe.d/iwlwifi.conf

# Show current loaded firmware
echo ""
echo "[+] Current firmware info:"
sudo dmesg | grep iwlwifi | grep firmware

# Regenerate initramfs
echo ""
echo "[+] Updating initramfs..."
sudo update-initramfs -u

echo ""
echo "[+] Reloading iwlwifi module..."
sudo modprobe -r iwlwifi && sudo modprobe iwlwifi

# 802-11-wireless.band bg forces the connection to only use 2.4 GHz.
# bg = 2.4 GHz only, a = 5 GHz only , any = both (default)
nmcli connection modify "Huawei_pKpM9W" 802-11-wireless.band bg
nmcli connection up "Huawei_pKpM9W"


echo ""
echo "[+] Done. Recommended: reboot your system to apply all changes."
read -p "Do you want to reboot now? (y/N): " REBOOT_NOW

if [[ "$REBOOT_NOW" == "y" || "$REBOOT_NOW" == "Y" ]]; then
  sudo reboot
else
  echo "[+] Reboot later with: sudo reboot"
fi
