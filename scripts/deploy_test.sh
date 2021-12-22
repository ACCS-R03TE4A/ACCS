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