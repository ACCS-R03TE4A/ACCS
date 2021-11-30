from flask import request
from flaskr.app import app


import json

from Comfortable_temperature_AI.src.TemperatureDetermination import TemperatureDetermination
from Home_appliance_control_AI.applianceControl import control
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
    


    #ACCS > temperature(Temperature) > Temperature(温度)からセンサ番号が0の最新を取り出す。

    tObject = Temperature.objects(temperatureCategory="0").first()
    tActual = tObject.Temperature    
    
    ####################################################################

    #目標温度が返ってくる...よね？
    tTarget = TemperatureDetermination(int(tActual),int(tSense))

    ################
    ittann = control(tActual,tTarget)


    return {"status":"200 OK","tActual":tActual,"tSense":tSense}
    #except Exception as e:
    #    print(e)#エラー
    #    return {"status":"400 Bad Request"}
    