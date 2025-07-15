#!/bin/bash

# ===================================================
# Kubuntu 25.04 | Install rclone + Google Drive mount (auto-mount at login)
# ===================================================

set -e

echo "==> Updating system..."
sudo apt update && sudo apt upgrade -y

echo "==> Installing curl, fuse3, and other deps..."
sudo apt install -y curl fuse3

echo "==> Downloading and installing latest rclone..."
curl https://rclone.org/install.sh | sudo bash

echo "==> Checking rclone version..."
rclone version

echo "==> Verifying FUSE version..."
fusermount3 --version || echo "FUSE3 not found! Make sure fuse3 is installed."

echo "==> Skipping 'fuse' group step: modern systems with FUSE3 do not use it."

echo "==> Ensuring /etc/fuse.conf has 'user_allow_other' uncommented..."
sudo sed -i 's/^#user_allow_other/user_allow_other/' /etc/fuse.conf

echo "==> Creating local Google Drive mount point..."
mkdir -p ~/GDrive

echo "==> Launching rclone config wizard..."
echo ">>> When prompted: [n] New remote -> Name it -> Choose 'drive' -> Follow OAuth."
rclone config

echo "==> Creating systemd user service to auto-mount Google Drive..."

mkdir -p ~/.config/systemd/user/

cat <<EOF > ~/.config/systemd/user/rclone-gdrive.service
[Unit]
Description=Rclone Mount for Google Drive
After=network-online.target

[Service]
Type=notify
ExecStart=/usr/bin/rclone mount \\
  --config=/home/%u/.config/rclone/rclone.conf \\
  --vfs-cache-mode writes \\
  --allow-other \\
  mygdrive: /home/%u/GDrive
ExecStop=/bin/fusermount3 -u /home/%u/GDrive
Restart=on-failure
Environment=XDG_RUNTIME_DIR=/run/user/%U

[Install]
WantedBy=default.target
EOF

echo "==> Reloading systemd user units..."
systemctl --user daemon-reload

echo "==> Enabling and starting rclone-gdrive user service..."
systemctl --user enable rclone-gdrive
systemctl --user start rclone-gdrive

echo "==> Checking status..."
systemctl --user status rclone-gdrive

echo "==> DONE!"
echo "Your Google Dri
