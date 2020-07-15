#!/bin/bash
# Only for Debian based system
sudo apt update && sudo apt ugprade -y
sudo apt install python3 python3-pip
pip3 install pipenv
pipenv install