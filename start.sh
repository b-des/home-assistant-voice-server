#!/bin/bash

# Ensure script is run with root privileges
if [[ $EUID -ne 0 ]]; then
    echo "Please run as root (or use sudo)"
    exit 1
fi

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
. venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install flask gunicorn streaming-stt-nemo gtts python-dotenv

# Copy systemd service file
cp assistant.service /etc/systemd/system/

# Reload systemd, enable, and start the service
systemctl daemon-reload
systemctl enable assistant.service
systemctl restart assistant.service  # Restart instead of start to ensure changes apply

echo "Setup completed successfully."
