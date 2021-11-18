from pymongo import MongoClient
from datetime import datetime
import os

from flask import Flask, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
) 

#
client = MongoClient()
#

#リモコンアプリからの温度感覚
@app.route("/temperatureSense", methods=["GET"])
def get_tSense():
    #try:
        tSense = request.args.get("tSense")
        if tSense == None:
            return {"status":"204 No Content"}
        
        #
        print(tSense)#コントロールサーバ


        #

        return {"status":"200 OK"}
    #except Exception as e:
    #    print(e)#エラー
    #    return {"status":"400 Bad Request"}
    

#センサモジュールからのセンサ番号、温度（室温、近辺温度）
@app.route("/temperatureActual", methods=["GET"])
def get_tActual():
    try:

        sNumber = request.args.get("sNumber")
        tActual = request.args.get("tActual")
        #all = request.args.getlist("")
        #?????????????????????????

        if sNumber == None or tActual == None:
            return {"status":"204 No Content"}
        
        #print(sNumber)#センサ番号
        #print(tActual)#温度データベースに登録
        client["ACCS"].temperature.insert_one({
            "time" : datetime.now(),
            "temperatureCategory" : int(sNumber),
            "Temperature" : float(tActual)
        })

        
        return {"status":"200 OK"}
    except Exception as e:
        print(e)#エラー
        return {"status":"400 Bad Request"}
    


#リモコンアプリからの郵便番号
@app.route("/postNumber", methods=["GET"])
def get_pNumber():
    #try:　　エラーが起こせないから消した
        pNumber = request.args.get("pNumber")
        if pNumber == None:
            return {"status":"204 No Content"}
        
        
        #print(pNumber)#郵便番号をデータベースに保存する。
        client["ACCS"].setting.insert_one({
            "postnumber" : pNumber
        })
        
        
        return {"status":"200 OK"}
    #except Exception as e:
    #    print(e)#エラー
    #    
    #    return {"status":"400 Bad Request"}



###############################################################

def create_app(test_config=None):
    # create and configure the app
#    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

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