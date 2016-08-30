#!/usr/bin/env bash

apt-get update
apt-get install python3 python-pip -y
cd /vagrant
pip install -r requirements.txt
python3 application.py > /var/log/athena