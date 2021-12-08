import json

import pytest
from unittest import mock
#from pytest_mock.plugin import MockFixture
from datetime import datetime
#from databases.collection_models.temperature import Temperature
from flaskr import create_app
from flaskr.databases.collection_models.queueOperation import queueOperation
from flaskr.databases.collection_models.temperature import Temperature

# def test_config():
#     assert not create_app().testingassert
#     create_app({'TESTING': True}).testing


@pytest.fixture(scope = 'function', autouse=True)
def scope_function():#いったんmocker抜いた
    #テスト前処理

    #テストのためだけの温度保存
    Temperature(
    time = "0001-01-01T01:01:01.000Z",
    temperatureCategory = 0,
    Temperature = 30 #この温度の場合
    ).save()

    # mocker.patch("flaskr.databases.collection_models.temperature.Temperature.objects.first", 
    # return_value=Temperature(time=datetime.now(),temperatureCategory = 0,Temperature=30))

    #queueOperationを空にする
    queueOperation.objects.all().delete()

    print("setup before session")
    yield
    #テスト後処理
    Temperature.objects(time = "0001-01-01T01:01:01.000Z").delete()

    print("teardown after session")



def test_tSense_0():
    app = create_app({'TESTING': True})
    client = app.test_client() 

    client.get('/temperatureSense?tSense=0')
    operation = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()
    x = int.from_bytes(operation.data, "big")
    ope = hex(x)
    
    operation.delete()
    assert ope == "0x17b00ff"


def test_tSense_1():
    app = create_app({'TESTING': True})
    client = app.test_client()

    client.get('/temperatureSense?tSense=1')
    operation = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()
    x = int.from_bytes(operation.data, "big")
    ope = hex(x)
    
    operation.delete()

    assert ope == "0x17b00ff"

#これヤバ()
# def test_tSense_2():#ちょうどいい
#     app = create_app({'TESTING': True})
#     client = app.test_client() 

#     client.get('/temperatureSense?tSense=2')

#     operation = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()
#     x = int.from_bytes(operation.data, "big")
#     ope = hex(x)
#     operation.delete()

#     assert ope == "0x17b10ef"


def test_tSense_3():
    app = create_app({'TESTING': True})
    client = app.test_client() 

    client.get('/temperatureSense?tSense=3')
    operation = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()
    x = int.from_bytes(operation.data, "big")
    ope = hex(x)
    operation.delete()

    operation2 = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()
    x = int.from_bytes(operation2.data, "big")
    ope2 = hex(x)
    operation2.delete()

    assert ope == "0x17b00ff"
    assert ope2 == "0x17b10ef"


def test_tSense_4():
    app = create_app({'TESTING': True})
    client = app.test_client() 
    
    client.get('/temperatureSense?tSense=4')
    operation = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()
    x = int.from_bytes(operation.data, "big")
    ope = hex(x)
    operation.delete()

    operation2 = queueOperation.objects(appliance="学校のサーキュレータ").order_by("+_id").first()
    x = int.from_bytes(operation2.data, "big")
    ope2 = hex(x)
    operation2.delete()

    assert ope == "0x17b00ff"
    assert ope2 == "0x17b10ef"
