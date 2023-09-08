from celery import shared_task
from datetime import datetime
import requests

from config import settings
from main.models import Habit

telegram_api_token = settings.TELEGRAM_API_TOKEN
chat_id = settings.CHAT_ID





@shared_task
def send_telegram_message(habit_id):
    habit = Habit.objects.get(id=habit_id)  # Получаем привычку по ее id
    # habit_time = habit.time  # Получаем время, когда нужно выполнить привычку
    now = datetime.now().time()  # Получаем текущее время
    # seconds_until_habit = (datetime.combine(datetime.today(), habit_time) - datetime.combine(datetime.today(), now)).total_seconds()  # Вычисляем количество секунд до нужного времени выполнения привычки
    message = (f"Напоминание о привычке для пользователя {habit.user.telegram_username}:\nМесто: {habit.place}\n"
               f"Действие: {habit.action}\nВремя: {habit.time}")  # Отправляем сообщение пользователю через телеграм
    url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        # "schedule_date": int(now.timestamp() + seconds_until_habit)
        "schedule_date": int(now.timestamp())
    }
    response = requests.get(url, params=params)

@shared_task
def check_message_time():
    now = datetime.now().time()  # Получаем текущее время
    habit = Habit.objects.all()  # Получаем все привычки
    for item in habit:  # Проходим по всем привычкам
        seconds_until_habit = (datetime.combine(datetime.today(), item.time) - datetime.combine(datetime.today(),
                                                                                                 now)).total_seconds()
        if -30 < seconds_until_habit < 29:  # Если время привычки приблизительно совпадает с текущим временем
            send_telegram_message(item.id)  # Запускаем отправку сообщения

