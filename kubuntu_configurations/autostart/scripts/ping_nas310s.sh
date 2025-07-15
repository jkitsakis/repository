#!/usr/bin/env bash

echo "[NAS310S] Ping script started..."

# Wait until the NAS responds to ping
until ping -c1 192.168.1.50 >/dev/null 2>&1; do
  echo "[NAS310S] Waiting for NAS network..."
  sleep 5
done

# Trigger automount
until ls ~/NAS310S > /dev/null 2>&1; do
  echo "[NAS310S] Waiting for automount to work..."
  sleep 5
done

echo "[NAS310S] NAS310S mounted successfully!"
