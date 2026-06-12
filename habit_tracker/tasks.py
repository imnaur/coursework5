from datetime import datetime
from django.utils import timezone

from celery import shared_task

from .models import Habit
from .services import send_reminder_in_tg


@shared_task
def check_habits():
    """Функция проверяет каждую минуту наличие привычки"""
    now = timezone.now()
    current_time = now.strftime('%H:%M')

    habits_to_remind = Habit.objects.filter(time=current_time)
    for habit in habits_to_remind:
        message = f"Напоминание! Пора выполнить привычку: {habit.action} в {habit.location}."
        if habit.user.chat_id:
            send_reminder_in_tg.delay(habit.user.chat_id, message)
