from flaskr import create_app

def test_200_temperatureSense():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/remocon')
    assert response.status_code >= 200