from flask import request, Response
from flaskr.app import app
from flaskr.databases.collection_models.queueOperation import queueOperation
import traceback
import json
from logging import getLogger, config


logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))

def digitConversion(x):
    y = int.from_bytes(x, "big")
    z = hex(y)
    return z

#{status:0 or 0以外}で指示があるかないかを判別させる
#status = データベースの要素数

@app.route("/operation", methods=["GET"])
def get_data():
    try:

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
            logger.info(dict_ope)

            #16進数への変換
            x = digitConversion(operation.data)
            dict_ope["data"] = x
            logger.info(dict_ope)
            #

            operation.delete()

            # print(f"operation={operation}")

            return {"status":d, "operation":dict_ope}
        
        else:
            return{"status":d}
        
    except Exception as e:
        traceback.print_exc() #エラー
        return Response(response=json.dumps({"status":"400 Bad Request"}), status=400)