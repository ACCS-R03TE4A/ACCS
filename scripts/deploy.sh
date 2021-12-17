#!/bin/bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
git submodule init
git submodule update
export FLASK_APP=flaskr
export FLASK_ENV=development
mongorestore --db="ACCS" dump/ACCS_DUMP/ 
git clone https://github.com/ACCS-R03TE4A/Remote-control-app.git
cd Remote-control-app
npm install
npm run build
cp -r build ../resources/
flask run -h 0.0.0.0
