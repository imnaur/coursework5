import requests
from celery import shared_task

from config import settings


@shared_task
def send_reminder_in_tg(chat_id, message):
    """Функция по отправке сообщения напоминания привычки (в тг)"""
    params = {"chat_id": chat_id, "text": message}
    requests.post(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_API}/sendMessage", params=params
    )
