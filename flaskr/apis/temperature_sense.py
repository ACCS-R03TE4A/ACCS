from flask import request
from flaskr.app import app

#リモコンアプリからの温度感覚
@app.route("/temperatureSense", methods=["GET"])
def get_tSense():
    #try:
    tSense = request.args.get("tSense")
    
    if tSense == None:
        return {"status":"204 No Content"}
    
    if int(tSense) < 1 or int(tSense) > 5:
        return {"status":"412 Precondition Failed"}
    


    #体感温度を1~5を引数に"TemperatureDetermination.py"を呼び出す
    print(tSense)
    
    #



    return {"status":"200 OK"}
    #except Exception as e:
    #    print(e)#エラー
    #    return {"status":"400 Bad Request"}
    