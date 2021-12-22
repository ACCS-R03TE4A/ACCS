from flaskr import create_app
import pytest
import json
import pytest
from flaskr.databases.collection_models.temperature import Temperature
from datetime import datetime

@pytest.fixture(scope = 'module', autouse=True)
def scope_module():
    print()
    print(f"-----------------{__name__}のテスト-----------------")
    print("Init \"temperature\" collection ")
    Temperature.objects.all().delete()
    print("Insert test data into \"temperature\" collection.")
    Temperature(
        time = datetime.now(),
        temperatureCategory = 0,
        Temperature = 22).save()
    yield
    print(f"--------------------------------------------------------")
    print()

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

#def test_hello():
#   app = create_app({'TESTING': True})
#    client = app.test_client() 
#    response = client.get('/hello')
#    assert response.data == b'Hello, World!'





def test_200_temperatureSense1():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureSense?tSense=0')
    data = json.loads(response.data)
    assert data["status"] == "200 OK"


def test_200_temperatureSense2():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureSense?tSense=4')
    data = json.loads(response.data)
    assert data["status"] == "200 OK"


def test_204_temperatureSense():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureSense')
    data = json.loads(response.data)
    assert data["status"] == "204 No Content"


def test_412_temperatureSense1():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureSense?tSense=-1')
    data = json.loads(response.data)
    assert data["status"] == "412 Precondition Failed"


def test_412_temperatureSense2():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureSense?tSense=5')
    data = json.loads(response.data)
    assert data["status"] == "412 Precondition Failed"


#################################################################

def test_200_temperatureActual():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureActual?sNumber=0&tActual=24')
    data = json.loads(response.data)
    assert data["status"] == "200 OK"


def test_204_temperatureActual():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureActual')
    data = json.loads(response.data)
    assert data["status"] == "204 No Content"


def test_412_temperatureActual():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureActual?sNumber=5&tActual=16')
    data = json.loads(response.data)
    assert data["status"] == "412 Precondition Failed"


def test_400_temperatureActual():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureActual?sNumber=&tActual=')
    data = json.loads(response.data)
    assert data["status"] == "400 Bad Request"




####################################################################

def test_200_postNumber():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/postNumber?pNumber=960-8253')
    data = json.loads(response.data)
    assert data["status"] == "200 OK"


def test_204_postNumber():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/postNumber')
    data = json.loads(response.data)
    assert data["status"] == "204 No Content"




