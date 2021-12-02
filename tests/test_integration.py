from flaskr import create_app
import pytest
import json


from flaskr import create_app
import pytest
import json


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_tSense_1():
    app = create_app({'TESTING': True})
    client = app.test_client() 

    response = client.get('/temperatureSense?tSense=1')
    data = json.loads(response.data)
    assert data["status"] == "200 OK"  #temperatureSense
    #assert


