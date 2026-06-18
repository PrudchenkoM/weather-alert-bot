import requests
from config import TOKEN, CHAT_ID


def send_message(message):

    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    telegram_data = {
        "chat_id": CHAT_ID,
        "text": message
    }


    response = requests.post(
        telegram_url,
        data=telegram_data
    )


    return response.status_code