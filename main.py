import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def write_log(message):
    time_now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    with open("logs.txt", "a", encoding="utf-8") as file:
        file.write(f"{time_now} | {message}\n")

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

weather_url = "https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.61&current_weather=true"



try:
    response = requests.get(weather_url)
    data = response.json()

    temperature = data["current_weather"]["temperature"]
    write_log("API OK")


    if temperature < 0:
        status = "🥶 Холодно, одевайся теплее"
    elif temperature < 15:
        status = "🧥 Прохладно"
    else:
        status = "☀️ Тепло"

    message = f"""
🌤 Погода

🌡 Температура: {temperature}°C
{status}
"""

except Exception as error:

    message = "❌ Ошибка получения погоды"
    write_log(f"API ERROR: {error}")

telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

telegram_data = {
    "chat_id": CHAT_ID,
    "text": message
}

telegram_response = requests.post(telegram_url, data=telegram_data)
if telegram_response.status_code == 200:
    write_log("Telegram sent")
else:
    write_log("Telegram error")

print(telegram_response.status_code)