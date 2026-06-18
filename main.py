from weather import get_weather
from logger import write_log
from telegram import send_message



try:
    temperature = get_weather()

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



status_code = send_message(message)


if status_code == 200:
    write_log("Telegram sent")
else:
    write_log("Telegram error")


print(status_code)