from flask import request
from flaskr.app import app
# from flaskr.databases.db import db
from flaskr.databases.collection_models.Setting import Setting

#リモコンアプリからの郵便番号
@app.route("/postNumber", methods=["GET"])
def get_pNumber():
    #try:　　エラーが起こせないから消した
        pNumber = request.args.get("pNumber")
        if pNumber == None:
            return {"status":"204 No Content"}
        
        
        print(pNumber)#郵便番号をデータベースに保存する。


        # client["ACCS"].setting.insert_one({
        #     "postnumber" : pNumber
        # })




        # id = client["ACCS"].setting.find()[0]
        # print(id)


        #id = client["ACCS"].setting.find()[0]["_id"]
        # id = "py9BZNHF6"

        # db.setting.update_one({"_id": id}, 
        # {"$set":{"postnumber":pNumber}},
        # upsert = True)

        Setting.objects.first().update(postnumber=pNumber)
        
        return {"status":"200 OK"}

    #except Exception as e:
    #    print(e)#エラー
    #    
    #    return {"status":"400 Bad Request"}