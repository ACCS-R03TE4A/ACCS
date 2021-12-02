from flask import request
from flaskr.app import app
# from flaskr.databases.db import db
from flaskr.databases.collection_models.queueOperation import queueOperation
import traceback
import json

#{status:0 or 1}で指示があるかないかを判別サセル
#
#

@app.route("/operation", methods=["GET"])
def get_data():
    try:
        ga = request.args.get("ga")
        if ga == None:
            return {"status":"204 No Content"}
        print(ga)


        try:
            d = len(queueOperation.objects(appliance="学校のサーキュレータ"))
        except AttributeError:
            d = 0
        
        if d != 0:
            operation = queueOperation.objects(appliance="学校のサーキュレータ").order_by("-_id").first()
            print(operation)
            operation.delete()
            return {"status":d, "operation":operation.get_dict()}

        else:
            return{"status":d}
    

    except Exception as e:
        traceback.print_exc() #エラー
        return {"status":"400 Bad Request"}