import requests

from config import settings

telegram_api_token = settings.TELEGRAM_API_TOKEN
chat_id = settings.CHAT_ID
#message = "Напоминание о привычке"
#
#url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
#params = {
#    "chat_id": chat_id,
#    "text": message
#}
#
#response = requests.get(url, params=params)
#print(response.json())

def send_telegram_message(habit):
    message = f"Ваша привычка: {habit.user.telegram_username}:\nМесто: {habit.place}\nДействие: {habit.action}\nВремя: {habit.time}"
    url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.get(url, params=params)
    return response.json()
