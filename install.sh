#!/bin/bash
apt update && apt install -y python3 python3-pip git
git clone https://github.com/xyzval/mbot.git
cd mbot
pip3 install -r requirements.txt
chmod +x run.sh
nohup bash run.sh
echo "✅ Bot terinstal dan berjalan."
