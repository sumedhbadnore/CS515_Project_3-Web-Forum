#!/bin/sh

python3 -m pip install --upgrade pip
pip3 install flask
apt-get update
apt-get install npm
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
apt-get install -y nodejs
# npm install -g newman