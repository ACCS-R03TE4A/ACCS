from flask import request
from flaskr.app import app

#リモコンアプリからの温度感覚
@app.route("/temperatureSense", methods=["GET"])
def get_tSense():
    #try:
    tSense = request.args.get("tSense")
    if tSense == None:
        return {"status":"204 No Content"}
    
    #
    print(tSense)


    #

    return {"status":"200 OK"}
    #except Exception as e:
    #    print(e)#エラー
    #    return {"status":"400 Bad Request"}
    