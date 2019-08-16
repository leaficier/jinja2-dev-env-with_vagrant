#!/bin/bash

echo "############[Installing Flask and shit]"
apt-get update
apt-get install -y python python-pip
pip install --upgrade pip
python -m pip install Flask jinja2

sleep 4
echo "############[DONE]"
