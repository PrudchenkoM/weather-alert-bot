import requests
from config import WEATHER_URL


def get_weather():

    response = requests.get(WEATHER_URL)

    data = response.json()

    temperature = data["current_weather"]["temperature"]

    return temperature