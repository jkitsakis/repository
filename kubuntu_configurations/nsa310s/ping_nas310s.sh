#!/usr/bin/env bash

until ls ~/NAS310S > /dev/null 2>&1; do
  echo "Waiting for NAS..."
  sleep 5
done
