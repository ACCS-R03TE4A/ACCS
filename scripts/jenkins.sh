#!/bin/bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pytest
ssh 192.168.1.83 "rm -rf ACCS-SERVER"
ssh 192.168.1.83 "git clone https://github.com/ACCS-R03TE4A/ACCS-SERVER.git"
ssh 192.168.1.83 "source ~/.profile;cd ACCS-SERVER;chmod +x ./scripts/deploy.sh;./scripts/deploy.sh"