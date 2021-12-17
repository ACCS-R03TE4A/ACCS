#!/bin/bash
apt install -y python3-venv
apt install -y build-essential
apt install -y python3-dev
apt install -y libffi-dev
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
apt-get update
apt-get install -y mongodb-org
wget -qO - https://deb.nodesource.com/setup_lts.x | bash -
apt install -y nodejs
systemctl start mongod
systemctl enable mongod
