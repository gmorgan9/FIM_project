#!/bin/bash

# Ensure the script is run as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root"
    exit 1
fi

# Stop and disable the service
systemctl stop file_integrity_monitor.service
systemctl disable file_integrity_monitor.service

# Remove the service file
rm /etc/systemd/system/file_integrity_monitor.service

rm /usr/local/bin/automate.py

rm /usr/local/bin/fim_tool/directories.txt

# Reload systemd to reflect changes
systemctl daemon-reload

echo "File Integrity Monitoring Service uninstalled."
