#!/usr/bin/env bash

# -----------------------------------
# CONFIGURATION
# -----------------------------------
NAS_IP="192.168.1.50"
SHARE_NAME="Volume1"  # <-- e.g., 'public', 'volume1'
MOUNT_POINT="$HOME/NAS310S"
CREDENTIALS_FILE="$HOME/.smbcredentials"
NAS_USERNAME="admin"
NAS_PASSWORD="exantas73"
SMB_VERSION="1.0"  # 1.0 for old NAS, or 2.0/3.0 if supported

# -----------------------------------
# CREATE MOUNT POINT
# -----------------------------------
echo "Creating mount point: $MOUNT_POINT"
mkdir -p "$MOUNT_POINT"

# -----------------------------------
# CREATE SMB CREDENTIALS FILE
# -----------------------------------
echo "Creating SMB credentials file: $CREDENTIALS_FILE"
cat <<EOF > "$CREDENTIALS_FILE"
username=$NAS_USERNAME
password=$NAS_PASSWORD
EOF
chmod 600 "$CREDENTIALS_FILE"

# -----------------------------------
# CREATE .mount UNIT
# -----------------------------------
MOUNT_UNIT_NAME="$(systemd-escape -p --suffix=mount "$MOUNT_POINT")"
MOUNT_UNIT_PATH="/etc/systemd/system/$MOUNT_UNIT_NAME"

echo "Creating systemd .mount unit: $MOUNT_UNIT_PATH"
sudo tee "$MOUNT_UNIT_PATH" > /dev/null <<EOF
[Unit]
Description=Mount NAS310S Share at $MOUNT_POINT
After=network-online.target
Wants=network-online.target

[Mount]
What=//${NAS_IP}/${SHARE_NAME}
Where=${MOUNT_POINT}
Type=cifs
Options=credentials=${CREDENTIALS_FILE},iocharset=utf8,vers=${SMB_VERSION},uid=$(id -u),gid=$(id -g)
TimeoutSec=30

[Install]
WantedBy=multi-user.target
EOF

# -----------------------------------
# CREATE .automount UNIT
# -----------------------------------
AUTOMOUNT_UNIT_NAME="$(systemd-escape -p --suffix=automount "$MOUNT_POINT")"
AUTOMOUNT_UNIT_PATH="/etc/systemd/system/$AUTOMOUNT_UNIT_NAME"

echo "Creating systemd .automount unit: $AUTOMOUNT_UNIT_PATH"
sudo tee "$AUTOMOUNT_UNIT_PATH" > /dev/null <<EOF
[Unit]
Description=Automount NAS310S Share at $MOUNT_POINT
After=network-online.target
Wants=network-online.target

[Automount]
Where=${MOUNT_POINT}

[Install]
WantedBy=multi-user.target
EOF

# -----------------------------------
# RELOAD SYSTEMD & ENABLE UNITS
# -----------------------------------
echo "Reloading systemd daemon..."
sudo systemctl daemon-reload

echo "Enabling and starting automount..."
sudo systemctl enable --now "$AUTOMOUNT_UNIT_NAME"

echo ""
echo "✅ Done!"
echo "Test by accessing: $MOUNT_POINT"
echo "Check status: systemctl status $AUTOMOUNT_UNIT_NAME"
