#!/bin/bash
# wifi_diagnostic.sh
# Basic Wi-Fi diagnostics for unstable/restarting connections

echo "=== [1] Listing network interfaces ==="
nmcli device status
echo "---------------------------------------"

echo "=== [2] Checking wireless interfaces ==="
iw dev
echo "---------------------------------------"

echo "=== [3] Current Wi-Fi connection status ==="
nmcli connection show --active
echo "---------------------------------------"

echo "=== [4] Checking signal strength and link info ==="
for iface in $(iw dev | awk '$1=="Interface"{print $2}'); do
    echo "-> Interface: $iface"
    iwconfig $iface
    iw $iface link
    echo "---------------------------------------"
done

echo "=== [5] Checking loaded Wi-Fi kernel modules ==="
lsmod | grep -E '88|iwlwifi|rtl|rtw|bcma|brcm'
echo "---------------------------------------"

echo "=== [6] Recent NetworkManager logs ==="
journalctl -u NetworkManager --since "5 min ago" | tail -n 50
echo "---------------------------------------"

echo "=== [7] Power management status ==="
for iface in $(iw dev | awk '$1=="Interface"{print $2}'); do
    echo "-> Interface: $iface"
    iwconfig $iface | grep "Power Management"
done

echo "=== [END] ==="
