from flask import request, Response
from flaskr.app import app
# from flaskr.databases.db import db
from flaskr.databases.collection_models.setting import Setting
import json

from logging import getLogger, config
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))


#現状DBがあれば動く
#DBへの追加でのエラー

#リモコンアプリからの郵便番号
#1 : 現在登録されている郵便番号の取得  ->  pNumber = get_pNumber() or requests.get(f"HTTP://localhost:5000/postNumber)
#2 : 追加や変更  ->  requests.get(f"HTTP://localhost:5000/postNumber?pNumber=○○○○○○○)
@app.route("/postNumber", methods=["GET"])

def get_pNumber():
    try:
        pNumber = request.args.get("pNumber")
        Object = Setting.objects().order_by("-time").first()

        #1 pNumberの入力なし
        if pNumber == None:

            #Object = Setting.objects().order_by("-time").first()

            #DBに未保存
            if Object == None:
                #ページ遷移がないだけで204は出ている
                return Response(response=json.dumps({"status":"204 No Content"}), status=204)
            
            pNumber = Object.postnumber
            return {"postNumber" : pNumber}
            
        #2 郵便番号をデータベースに保存する。
        if Object == None:
            Setting(postnumber=pNumber).save()
        else:
            Setting.objects.first().update(postnumber=pNumber)

        return Response(response=json.dumps({"status":"200 OK"}), status=200)
    except Exception as e:
        logger.info(e)#エラー
        return Response(response=json.dumps({"status":"400 Bad Request"}), status=400)