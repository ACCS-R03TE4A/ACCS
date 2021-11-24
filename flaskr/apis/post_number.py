from flask import request
from flaskr.app import app
# from flaskr.databases.db import db
from flaskr.databases.collection_models.setting import Setting

#リモコンアプリからの郵便番号
@app.route("/postNumber", methods=["GET"])
def get_pNumber():
    #try:　　エラーが起こせないから消した
        pNumber = request.args.get("pNumber")
        if pNumber == None:
            return {"status":"204 No Content"}
        
        
        print(pNumber)#郵便番号をデータベースに保存する。




        Setting.objects.first().update(postnumber=pNumber)
        
        return {"status":"200 OK"}

    #except Exception as e:
    #    print(e)#エラー
    #    
    #    return {"status":"400 Bad Request"}