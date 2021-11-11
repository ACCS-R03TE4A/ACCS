#!/bin/bash
python3 -m venv env
source env/bin/activate
pip isntall -r requirements.txt
pytest