from flask import config
from pymongo import MongoClient
from datetime import datetime
import os


from flask_cors import CORS
from flaskr.app import app

# view
import flaskr.views.remocon
import flaskr.views.redirect_to_remocon

# API
import flaskr.apis.post_number
import flaskr.apis.temperature
import flaskr.apis.temperature_sense
import flaskr.apis.operation
import flaskr.apis.temperature_current

# Database
import flaskr.databases.db
from flaskr.databases.collection_models.setting import Setting


#logger
from flaskr.logger import initLogger
initLogger()


CORS(
    app,
    supports_credentials=True
) 

if app.env != "test":
    import flaskr.build_and_deploy_remocon_app # リモコンアプリのビルドと配置をする。

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