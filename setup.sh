#!/bin/sh

python3 -m pip install --upgrade pip
pip3 install flask
apt-get update
apt-get install nodejs16 npm
# npm install -g newman