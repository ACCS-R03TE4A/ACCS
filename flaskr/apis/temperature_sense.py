from flask import request, Response
from flaskr.app import app

import json
import requests

from Comfortable_temperature_AI.src.TemperatureDetermination import TemperatureDetermination
from Home_appliance_control_AI.applianceControl import control
from flaskr.databases.collection_models.temperature import Temperature
from flaskr.util.temperatureCategory import TemperatureCategory

from logging import getLogger, config
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))

#リモコンアプリからの温度感覚``
@app.route("/temperatureSense", methods=["GET"])
def get_tSense():
    #try:
    tSense = request.args.get("tSense")
    
    if tSense == None:
        return  Response(response=json.dumps({"status":"204 No Content"}), status=204)
    
    if int(tSense) < 0 or int(tSense) > 4:
        return Response(response=json.dumps({"status":"412 Precondition Failed"}), status=412)
    


    #ACCS > temperature(Temperature) > Temperature(温度)からセンサ番号が0(近辺温度)の最新を取り出す。
    tObject = Temperature.objects(temperatureCategory= TemperatureCategory.tActual).order_by("-time").first()
    tActual = tObject.Temperature
    
    #Determinationから目標温度が返ってくる
    tTarget = TemperatureDetermination(int(tActual),int(tSense)).decision_base()
    logger.info(tTarget)

    #目標温度の保存
    requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tTarget}&tActual={tTarget}")

    #ちょうどいいが選択された場合のみ快適温度を保存する
    if tSense == 2: 
        requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber=sNumber={TemperatureCategory.tSuitable}&tActual={tActual}")
        logger.info("快適温度を保存")

    #操作指示
    controlResult = control(tActual,tTarget)

    
    return Response(response=json.dumps({"status":"200 OK","tActual":tActual,"tSense":tSense}), status=200)
    #return {"status":"200 OK","tActual":tActual,"tSense":tSense}

    #except Exception as e:
    #    logger.info(e)#エラー
    #    return {"status":"400 Bad Request"}
    