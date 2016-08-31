#!/usr/bin/env bash

apt-get update
apt-get install python3 python-pip -y
cd /vagrant
pip install -r requirements.txt
python3 application.py --awsKey=$1 --awsSecret=$2 --sqsHost=$3 --sqsHost=$4 > /var/log/athena