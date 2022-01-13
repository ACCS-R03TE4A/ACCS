from flask import request, Response
from flaskr.app import app

import json
import requests
import time
import threading
from datetime import datetime, timedelta

from Comfortable_temperature_AI.src.TemperatureDetermination import TemperatureDetermination
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



#リモコンアプリからの温度感覚``
@app.route("/temperatureSense", methods=["GET"])
def timeLimit():
    global isPressedSuitable
    timer_start = None
    timeFrag = 0
    while not isPressedSuitable:
        tObject = Temperature.objects(temperatureCategory= TemperatureCategory.tActual).order_by("-time").first()
        tActual = tObject.Temperature
        tObject2 = Temperature.objects(temperatureCategory= TemperatureCategory.tTarget).order_by("-time").first()
        tTarget = tObject.Temperature

        if timeFrag == 0:
            if (tempDiff > 0 and tActual >= tTarget) or (tempDiff < 0 and tActual <= tTarget):
                timer_start = datetime.now()
                timeFrag = 1

        if timeFrag == 1:
            if datetime.now() - timer_start >= timedelta(minutes=10):
                requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tSuitable}&tActual={tActual}")
                logger.info("快適温度を保存")
                isPressedSuitable = True
            time.sleep(1)



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
    tTarget = TemperatureDetermination(int(tActual),int(tSense)).decision_base()
    logger.info(tTarget)

    global tempDiff
    tempDiff = tTarget - tActual

    #目標温度の保存
    requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tTarget}&tActual={tTarget}")

    #ちょうどいいが選択された場合のみ快適温度を保存する
    if tSense == 2: 
        requests.get(f"HTTP://localhost:5000/temperatureActual?sNumber={TemperatureCategory.tSuitable}&tActual={tActual}")
        logger.info("快適温度を保存")
        global isPressedSuitable
        isPressedSuitable = True
    else:
        isPressedSuitable = False
        global timer
        if timer != None:
            isPressedSuitable = True
            timer.join()
        timer = threading.Thread(target=timeLimit)
        timer.start()


    #操作指示
    control(tActual,tTarget)

    
    return Response(response=json.dumps({"status":"200 OK","tActual":tActual,"tSense":tSense}), status=200)





if __name__ == "__main__":
    thread_1 = threading.Thread(target = get_tSense)
    thread_2 = threading.Thread(target = timeLimit)

    thread_1.start()
    thread_2.start()




