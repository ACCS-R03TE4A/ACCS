from pymongo import MongoClient
from datetime import datetime
import os


from flask_cors import CORS
from flaskr.app import app

import threading
import sampleOutsideTemp

import flaskr.views.remocon
import flaskr.apis.post_number
import flaskr.apis.temperature
import flaskr.apis.temperature_sense
import flaskr.apis.operation

# from flaskr.databases.db import db
import flaskr.databases.db
from flaskr.databases.collection_models.setting import Setting

from flask.helpers import send_from_directory


CORS(
    app,
    supports_credentials=True
) 


#郵便番号をデータベースからとってくる
# id = "py9BZNHF6"
# pn = db.setting.find_one({"_id": id})["postnumber"]
if Setting.objects.all().count() == 0:
    print(Setting(postnumber="980-0013").save())
pn = Setting.objects.first().postnumber
# threading.Thread(target=sampleOutsideTemp.task, args=(pn,)).start()

###############################################################

def create_app(test_config=None):
    # create and configure the app
#    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    return app