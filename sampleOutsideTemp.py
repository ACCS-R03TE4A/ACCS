import time
import requests
from flaskr.util.SearchTemperature import get_temperature
def task(postNumber):
    while True:
        temp = get_temperature(postNumber)
        requests.get(f"http://localhost:5000/temperatureActual?sNumber=2&tActual={temp}")
        time.sleep(10 * 60)