import requests
from config import settings
from habits.models import Habit
from celery import shared_task


@shared_task
def send_message_to_bot(habit_id):
    """
    Отправляет сообщение о привычке в телеграм бот
    """
    habit = Habit.objects.get(id=habit_id)
    requests.get(
        url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
        params={
            'chat_id': habit.creator.telegram,
            'text': f'Cделать {habit.action} в {habit.time} в {habit.place}.'
        }
    )
