from flaskr import create_app
import pytest

@pytest.fixture(scope = 'module', autouse=True)
def scope_module():
    print()
    print(f"-----------------{__name__}のテスト-----------------")
    yield
    print(f"--------------------------------------------------------")
    print()

def test_200_temperatureSense():
    app = create_app({'TESTING': True})

    client = app.test_client() 
    response = client.get('/remocon')
    assert response.status_code >= 200