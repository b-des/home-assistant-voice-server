#!/bin/bash

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
. venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install flask gunicorn streaming-stt-nemo gtts python-dotenv

# Ask for sudo password only when required
echo "Requesting root privileges for systemd setup..."
sudo cp assistant.service /etc/systemd/system/

# Reload systemd, enable, and start the service with sudo
sudo systemctl daemon-reload
sudo systemctl enable assistant.service
sudo systemctl restart assistant.service

echo "Setup completed successfully."
