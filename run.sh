#!/bin/bash
pkill -f bot.py
nohup python3 bot.py &> bot.log &
echo "Bot dijalankan (lihat bot.log)."
