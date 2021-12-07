from flask import request
from flaskr.app import app
# from flaskr.databases.db import db
from flaskr.databases.collection_models.queueOperation import queueOperation
import traceback
import json
import binascii

def digitConversion(x):
    y = int.from_bytes(x, "big")
    z = hex(y)
    return z

#{status:0 or 0以外}で指示があるかないかを判別させる
#status = データベースの要素数

@app.route("/operation", methods=["GET"])
def get_data():
    try:
        #値がほしくなったら「?value」にでも入れる。
        # value = request.args.get("value")
        # if value == None:
        #     return {"status":"204 No Content"}
        # print(value)

        #操作キューデータベースの中身確認
        try:
            d = len(queueOperation.objects(appliance="学校のサーキュレータ"))
        except AttributeError:
            d = 0
        #

        #ObjectIdは作成タイムスタンプをカプセル化するため、ObjectIdで直接並べ替えることができます。
        #これは、作成日時によって自然に並べ替えられます。
        if d != 0:
            operation = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()

            dict_ope = operation.get_dict()
            print(dict_ope)

            #16進数への変換
            x = digitConversion(operation.data)
            dict_ope["data"] = x
            print(dict_ope)
            #

            operation.delete()
            return {"status":d, "operation":dict_ope}
        
        else:
            return{"status":d}
        
    except Exception as e:
        traceback.print_exc() #エラー
        return {"status":"400 Bad Request"}