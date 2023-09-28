import datetime

from celery import shared_task

from habits.models import Habit
from utils.telegram import send_message


@shared_task
def check_habits():
    now_hour = datetime.datetime.now().hour
    now_min = datetime.datetime.now().minute
    habits = Habit.objects.filter(
        time__hour=now_hour,
        time__minute=now_min
    )
    for habit in habits:
        action = habit.action
        place = habit.place
        time = habit.time
        user_tg = habit.author.telegram_name

        send_message(user_tg,
                     f'Напоминание: нужно {action} в {place} в {time}')
