#!/bin/bash

# Ensure the script is run as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root"
    exit 1
fi

# Copy automate.py to a suitable location
mkdir /usr/local/bin/fim_tool
cp ../automate.py /usr/local/bin/fim_tool/automate.py
touch /usr/local/bin/fim_tool/directories.txt
chmod +x /usr/local/bin/automate.py

# Create a systemd service file
cat <<EOF > /etc/systemd/system/file_integrity_monitor.service
[Unit]
Description=File Integrity Monitoring Service
After=network.target

[Service]
User=root
ExecStart=python3 /usr/local/bin/automate.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd to load the new service file
systemctl daemon-reload

# Enable and start the service
systemctl enable file_integrity_monitor.service
systemctl start file_integrity_monitor.service

echo "File Integrity Monitoring Service installed and started."
