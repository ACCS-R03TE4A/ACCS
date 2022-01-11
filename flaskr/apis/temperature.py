from flask import json, request, Response
from flaskr.app import app
from datetime import datetime
from flaskr.databases.collection_models.temperature import Temperature

#センサモジュールからのセンサ番号、温度（室温、近辺温度）
#センサモジュールから定期的
@app.route("/temperatureActual", methods=["GET"])
def get_tActual():
    try:

        sNumber = request.args.get("sNumber")
        tActual = request.args.get("tActual")

        if sNumber == None or tActual == None:
            return Response(response=json.dumps({"status":"204 No Content"}), status=204) 
        
        if int(sNumber) < 0 or int(sNumber) > 4:
            return Response(response=json.dumps({"status":"412 Precondition Failed"}), status=412)
        
        #print(sNumber)#センサ番号
        #print(tActual)#温度データベースに登録
        # db.temperature.insert_one({
        #     "time" : datetime.now(),
        #     "temperatureCategory" : int(sNumber),
        #     "Temperature" : float(tActual)
        # })

        Temperature(
            time=datetime.now(),
            temperatureCategory=int(sNumber),
            Temperature=float(tActual)
            ).save()
        
        return {"status":"200 OK"}
    except Exception as e:
        print(e)#エラー
        return Response(response=json.dumps({"status":"400 Bad Request"}), status=400)