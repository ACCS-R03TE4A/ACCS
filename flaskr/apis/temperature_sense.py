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

    #1:帰ってくるのは"Temperature"　型っぽい。json対応してない
    #tActual = Temperature.objects(temperatureCategory="10").first()

    #2:取ってこれるけど、値が2つあるし、分けれない。
    #tActual = Temperature.objects.get(temperatureCategory="10")

    #3:全部出して最初だけ取り出しそう。"visitors"ないけど。
    #tActual = Temperature.objects.all()
    #tActual = visitors[0].ip

    #4:Temperature objectが返ってくる
    #tActual = Temperature.objects.first(Temperature)


    print(tActual)    

    
    #td = TemperatureDetermination(tActual,int(tSense))

    return {"status":"200 OK","tSense":tSense}
    #except Exception as e:
    #    print(e)#エラー
    #    return {"status":"400 Bad Request"}
    