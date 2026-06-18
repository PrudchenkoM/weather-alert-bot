from datetime import datetime


def write_log(message):

    time_now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    with open("logs.txt", "a", encoding="utf-8") as file:
        file.write(f"{time_now} | {message}\n")