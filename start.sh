python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp assistant.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable assistant.service
systemctl start assistant.service