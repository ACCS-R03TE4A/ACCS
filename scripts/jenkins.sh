#!/bin/bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
git submodule init
git submodule update
export FLASK_APP=flaskr
export FLASK_ENV=test
mongorestore --db="ACCS" dump/ACCS_DUMP/ 
pytest
# ssh 192.168.1.83 "rm -rf ACCS-SERVER"
# ssh 192.168.1.83 "git clone https://github.com/ACCS-R03TE4A/ACCS-SERVER.git"
# ssh 192.168.1.83 "source ~/.profile;cd ACCS-SERVER;chmod +x ./scripts/deploy.sh;./scripts/deploy_test.sh"