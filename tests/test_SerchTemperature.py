from flaskr.util.search_temperature import get_temperature
import pytest

@pytest.fixture(scope = 'module', autouse=True)
def scope_module():
    print()
    print(f"-----------------{__name__}のテスト-----------------")
    yield
    print(f"--------------------------------------------------------")
    print()

#input:郵便番号、output:float型の数値
def test_get_temperature():
    temperature = get_temperature("980-0021")
    assert isinstance(temperature, float) == True

def test_get_temperature_NGcase():
    temperature = get_temperature("980-0021")
    assert isinstance(temperature, int) == False

