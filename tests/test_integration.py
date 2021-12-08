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

@pytest.fixture(scope = 'module', autouse=True)
def scope_module():
    print()
    print(f"-----------------{__name__}のテスト-----------------")
    yield
    print(f"--------------------------------------------------------")
    print()

@pytest.fixture(scope = 'function', autouse=True)
def scope_function():#いったんmocker抜いた
    #テスト前処理
    print("setup before session")   
    #テストのためだけの温度保存
    Temperature(
    time = "0001-01-01T01:01:01.000Z",
    temperatureCategory = 0,
    Temperature = 30 #この温度の場合
    ).save()
    
    #queueOperationを空にする
    queueOperation.objects.all().delete()

    
    yield
    #テスト後処理
    Temperature.objects(time = "0001-01-01T01:01:01.000Z").delete()

    print("teardown after session")


def test_tSense_0():
    app = create_app({'TESTING': True})
    client = app.test_client() 

    client.get('/temperatureSense?tSense=0')
    response = client.get('/operation')
    actual = json.loads(response.data)

    assert actual['status'] == 1
    assert actual['operation']['data'] == '0x17b00ff'


def test_tSense_1():
    app = create_app({'TESTING': True})
    client = app.test_client()

    client.get('/temperatureSense?tSense=1')
    response = client.get('/operation')
    actual = json.loads(response.data)

    assert actual['status'] == 1
    assert actual['operation']['data'] == '0x17b00ff'

#test_tSense_2は適温 -> 操作なし

def test_tSense_3():
    app = create_app({'TESTING': True})
    client = app.test_client() 

    client.get('/temperatureSense?tSense=3')
    response = client.get('/operation')
    actual = json.loads(response.data)

    assert actual['status'] == 2
    assert actual['operation']['data'] == '0x17b00ff'


    response = client.get('/operation')
    actual = json.loads(response.data)

    assert actual['status'] == 1
    assert actual['operation']['data'] == '0x17b10ef'


def test_tSense_4():
    app = create_app({'TESTING': True})
    client = app.test_client() 
    
    client.get('/temperatureSense?tSense=4')
    response = client.get('/operation')
    actual = json.loads(response.data)

    assert actual['status'] == 2
    assert actual['operation']['data'] == '0x17b00ff'


    response = client.get('/operation')
    actual = json.loads(response.data)

    assert actual['status'] == 1
    assert actual['operation']['data'] == '0x17b10ef'

