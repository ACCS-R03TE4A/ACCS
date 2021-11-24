from flaskr import create_app
import pytest
import json


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
    response = client.get('/temperatureSense?tSense=1')
    data = json.loads(response.data)
    assert data["status"] == "200 OK"


def test_200_temperatureSense2():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureSense?tSense=5')
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
    response = client.get('/temperatureSense?tSense=0')
    data = json.loads(response.data)
    assert data["status"] == "412 Precondition Failed"


def test_412_temperatureSense2():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureSense?tSense=6')
    data = json.loads(response.data)
    assert data["status"] == "412 Precondition Failed"


#################################################################

def test_200_temperatureActual():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureActual?sNumber=10&tActual=555')
    data = json.loads(response.data)
    assert data["status"] == "200 OK"


def test_204_temperatureActual():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/temperatureActual')
    data = json.loads(response.data)
    assert data["status"] == "204 No Content"


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




