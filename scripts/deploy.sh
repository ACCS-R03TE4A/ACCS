#!/bin/bash
~/accs_setting.sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=flaskr
export FLASK_ENV=development
pytest
flask run