#!/bin/sh

python3 -m pip install --upgrade pip
pip3 install flask
apt-get update
apt-get install npm
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
apt-get install -y nodejs
# npm install -g newman