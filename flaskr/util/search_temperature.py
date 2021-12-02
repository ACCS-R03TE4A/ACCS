import requests
import json
import sys
import os
import re

def get_temperature(post_number): 
    API_KEY = os.environ['OpenWeather_API_KEY']
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
    
    try:
        #郵便番号はハイフンが入っている必要がある
        rx = re.match('[0-9]{3}-[0-9]{4}' , post_number)
        if bool(rx) == False:
             raise ValueError()
        url = api.format(city = post_number, key = API_KEY)
        data = requests.get(url).json()
        return data['main']['temp']
    except ValueError:
        return "PostNumber is out of range."
    
