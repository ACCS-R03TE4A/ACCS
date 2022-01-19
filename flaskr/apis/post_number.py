from flask import request, Response
from flaskr.app import app
# from flaskr.databases.db import db
from flaskr.databases.collection_models.setting import Setting
import json

from logging import getLogger, config
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))


#リモコンアプリからの郵便番号
#requestじゃない呼び出し方というか、直接メソッドとして呼ばれたときにDBに保存してある郵便番号を返す
#追加や変更は    requests.get(f"HTTP://localhost:5000/postNumber?pNumber=○○○○○○○
#現在登録されている郵便番号は    pNumber = get_pNumber()
@app.route("/postNumber", methods=["GET"])
def get_pNumber():
    try:
        pNumber = request.args.get("pNumber")
        if pNumber == None:
            Object = Setting.objects().order_by("-time").first()
            if Object == None:
                return Response(response=json.dumps({"status":"204 No Content"}), status=204)

            pNumber = Object.postnumber
            return pNumber
            
        #郵便番号をデータベースに保存する。
        Setting.objects.first().update(postnumber=pNumber)
        return Response(response=json.dumps({"status":"200 OK"}), status=200)
    except Exception as e:
        logger.info(e)#エラー
        return Response(response=json.dumps({"status":"400 Bad Request"}), status=400)