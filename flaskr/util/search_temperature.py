import requests
import json
import sys
import os

def get_temperature(postNumber): 
    API_KEY = os.environ['OpenWeather_API_KEY']
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
    
    #郵便番号はハイフン無いとダメ
    url = api.format(city = postNumber, key = API_KEY)
    data = requests.get(url).json()
    print(data)
    return data['main']['temp']