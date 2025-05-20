#!/bin/bash
apt update && apt install -y chromium-driver chromium
python3 bot.py
