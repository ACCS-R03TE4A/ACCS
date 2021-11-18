from flask import request
from flaskr.app import app
from flaskr.databases.db import db
from datetime import datetime

#センサモジュールからのセンサ番号、温度（室温、近辺温度）
#センサモジュールから定期的
@app.route("/temperatureActual", methods=["GET"])
def get_tActual():
    try:

        sNumber = request.args.get("sNumber")
        tActual = request.args.get("tActual")

        if sNumber == None or tActual == None:
            return {"status":"204 No Content"}
        
        #print(sNumber)#センサ番号
        #print(tActual)#温度データベースに登録
        db.temperature.insert_one({
            "time" : datetime.now(),
            "temperatureCategory" : int(sNumber),
            "Temperature" : float(tActual)
        })

        
        return {"status":"200 OK"}
    except Exception as e:
        print(e)#エラー
        return {"status":"400 Bad Request"}