from flask import request, Response
from flaskr.app import app

import requests
import json
import time
import threading
from datetime import datetime, timedelta

from Comfortable_temperature_AI.src.TemperatureDetermination import ComfortTemperaturePredictionAI
from Home_appliance_control_AI.applianceControl import control
from flaskr.databases.collection_models.temperature import Temperature
from flaskr.util.temperatureCategory import TemperatureCategory

from logging import getLogger, config
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))


isPressedSuitable = False
tempDiff = 0
timer = None

comfTempAI = ComfortTemperaturePredictionAI()

def timeLimit():
    logger.info("自動保存タスクスタート")
    global isPressedSuitable
    timer_start = None
    while not isPressedSuitable:
        tObject = Temperature.objects(temperatureCategory= TemperatureCategory.tActual).order_by("-time").first()
        tActual = tObject.Temperature
        tObject2 = Temperature.objects(temperatureCategory= TemperatureCategory.tTarget).order_by("-time").first()
        tTarget = tObject2.Temperature
        if timer_start == None:
            if (tempDiff > 0 and tActual >= tTarget) or (tempDiff < 0 and tActual <= tTarget):
                timer_start = datetime.now()
                logger.info("快適温度自動保存タイマースタート")
        else:
            # TODO timedelta(seconds=10) -> timedeleta(minutes=10)
            if datetime.now() - timer_start >= timedelta(seconds=10):

                requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tSuitable}&tActual={int(tActual)}")
                requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tTarget}&tActual={int(tActual)}")

                logger.info("快適温度の自動保存")
                isPressedSuitable = True
        time.sleep(1e-3)
    logger.info("タスク終了")


#リモコンアプリからの温度感覚``
@app.route("/temperatureSense", methods=["GET"])
def get_tSense():
    tSense = request.args.get("tSense")
    
    if tSense == None:
        return  Response(response=json.dumps({"status":"204 No Content"}), status=204)
    
    if int(tSense) < 0 or int(tSense) > 4:
        return Response(response=json.dumps({"status":"412 Precondition Failed"}), status=412)
    

    #ACCS > temperature(Temperature) > Temperature(温度)からセンサ番号が0(近辺温度)の最新を取り出す。
    tObject = Temperature.objects(temperatureCategory= TemperatureCategory.tActual).order_by("-time").first()
    tActual = tObject.Temperature
    
    #Determinationから目標温度が返ってくる
    tTarget = comfTempAI.getTargetTemperature(tSense)
    logger.info(tTarget)

    global tempDiff
    tempDiff = tTarget - tActual

    #目標温度の保存
    w = requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tTarget}&tActual={int(tTarget)}")

    #ちょうどいいが選択された場合のみ快適温度を保存する

    if tSense == "2": 
        requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tSuitable}&tActual={int(tActual)}")
        requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tTarget}&tActual={int(tActual)}")
        logger.info("ユーザが快適温度を保存")
        global isPressedSuitable
        isPressedSuitable = True

    else:
        global timer
        if timer != None:
            isPressedSuitable = True
            logger.info("古いタスクの終了待ち")
            timer.join()
        isPressedSuitable = False
        timer = threading.Thread(target=timeLimit)
        timer.start()


    #操作指示
    control(tActual,tTarget)

    
    return Response(response=json.dumps({"status":"200 OK","tActual":tActual,"tSense":tSense}), status=200)
