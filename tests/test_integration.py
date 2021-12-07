import json

import pytest
from flaskr import create_app
from flaskr.databases.collection_models.queueOperation import queueOperation

# def test_config():
#     assert not create_app().testingassert
#     create_app({'TESTING': True}).testing


def test_tSense_0():
    app = create_app({'TESTING': True})
    client = app.test_client() 

    #queueOperationを空にする
    queueOperation.objects.all().delete()

    client.get('/temperatureSense?tSense=0')
    operation = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()
    x = int.from_bytes(operation.data, "big")
    ope = hex(x)
    
    operation.delete()

    assert ope == "0x17b00ff"


#################################################################
