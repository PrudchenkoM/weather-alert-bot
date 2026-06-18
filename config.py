import os
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


WEATHER_URL = "https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.61&current_weather=true"