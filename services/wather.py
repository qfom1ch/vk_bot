import datetime
import json

import requests

from config import OWM_TOKEN


def get_weather_now(city):
    token = OWM_TOKEN

    code_to_smile = {
        "Clear": "Ясно",
        "Clouds": "Облачно",
        "Rain": "Дождь",
        "Drizzle": "Дождь",
        "Thunderstorm": "Гроза",
        "Snow": "Снег",
        "Mist": "Туман"
    }

    url = (f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid="
           f"{token}")
    response = requests.get(url)
    data = json.loads(response.text)

    temperature = str(data["main"]["temp"] - 273.15).split('.')[0]

    weather_description = data["weather"][0]["main"]
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = "непонятная погода, лучше посмотри в окно!"

    return wd, temperature


def get_weather_tomorrow(city):
    token = OWM_TOKEN

    code_to_smile = {
        "Clear": "Ясно",
        "Clouds": "Облачно",
        "Rain": "Дождь",
        "Drizzle": "Дождь",
        "Thunderstorm": "Гроза",
        "Snow": "Снег",
        "Mist": "Туман"
    }

    url = (f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid="
           f"{token}")
    response = requests.get(url)
    data = json.loads(response.text)
    res = []
    for i in data['list']:
        if int(i['dt_txt'][8:11]) - int(datetime.datetime.now().day) == 1:

            weather_description = i["weather"][0]["main"]
            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = "непонятная погода, лучше посмотри в окно!"

            res.append(
                f"{wd} {str(i['main']['temp'] - 273.15).split('.')[0]}")
    return tuple(res[len(res) // 2].split())
