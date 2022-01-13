from flask import request, Response
from flaskr.app import app

import json
import requests
import traceback

from Home_appliance_control_AI.applianceControl import control
from flaskr.databases.collection_models.temperature import Temperature
from flaskr.util.temperatureCategory import TemperatureCategory

from logging import getLogger, config
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))

#リモコンアプリからの温度感覚
@app.route("/temperatureCurrent", methods=["GET"])
def get_tCurrent():
    try:
        
        #各カテゴリの最新データ
        tCurrent_A = Temperature.objects(temperatureCategory= TemperatureCategory.tActual).order_by("-time").first() 
        tCurrent_I = Temperature.objects(temperatureCategory= TemperatureCategory.InsideTemp).order_by("-time").first()
        tCurrent_O = Temperature.objects(temperatureCategory= TemperatureCategory.OutsideTemp).order_by("-time").first()
        tCurrent_S = Temperature.objects(temperatureCategory= TemperatureCategory.tTarget).order_by("-time").first()
        

        logger.info({"status":"200 OK","tCurrent":{
            "InsideTemp":tCurrent_I.Temperature if tCurrent_I != None else None, 
            "OutsideTemp":tCurrent_O.Temperature if tCurrent_O != None else None, 
            "tActual":tCurrent_A.Temperature if tCurrent_A != None else None, 
            "tTarget":tCurrent_S.Temperature if tCurrent_S != None else None
            }})
        
        return {"status":"200 OK","tCurrent":{
            "InsideTemp":tCurrent_I.Temperature if tCurrent_I != None else "未取得", 
            "OutsideTemp":tCurrent_O.Temperature if tCurrent_O != None else "未取得", 
            "tActual":tCurrent_A.Temperature if tCurrent_A != None else "未取得", 
            "tTarget":tCurrent_S.Temperature if tCurrent_S != None else "未取得"
            }}
    except Exception as e:
        traceback.print_exc()
        return Response(responce=json.dumps({"status":"400 Bad Request"}), status=400)