from flask import request
from flaskr.app import app

import mongoengine

import json

from Comfortable_temperature_AI.src.TemperatureDetermination import TemperatureDetermination
from flaskr.databases.collection_models.temperature import Temperature


#リモコンアプリからの温度感覚
@app.route("/temperatureSense", methods=["GET"])
def get_tSense():
    #try:
    tSense = request.args.get("tSense")
    
    if tSense == None:
        return {"status":"204 No Content"}
    
    if int(tSense) < 1 or int(tSense) > 5:
        return {"status":"412 Precondition Failed"}
    

    #近辺温度(temperatureCategory=sNumber)が0のものが欲しい

    #ACCS > temperature(Temperature) > Temperature(温度)の最新を取り出す
    tObject = Temperature.objects(temperatureCategory="0").first()
    tActual = tObject.Temperature    
    
    td = TemperatureDetermination(int(tActual),int(tSense))

    return {"status":"200 OK","tActual":tActual,"tSense":tSense}
    #except Exception as e:
    #    print(e)#エラー
    #    return {"status":"400 Bad Request"}
    