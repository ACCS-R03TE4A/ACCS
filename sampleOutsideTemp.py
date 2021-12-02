import threading
import requests
from flaskr.util.search_temperature import get_temperature
import sys
from flaskr import app

def task(postNumber):
    temp = get_temperature(postNumber)
    try:
        requests.get(f"http://localhost:5000/temperatureActual?sNumber=2&tActual={temp}")
    except Exception as error:
        print(error, file=sys.stderr)
    app.task_thread = threading.Timer(5, task, args=(postNumber,))
    app.task_thread.start()