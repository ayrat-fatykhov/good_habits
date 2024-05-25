from datetime import timedelta

from django.core.exceptions import ValidationError


def habit_validators(value):
    """
    Проверяет взаимоисключающие поля модели Habit и вводит ограничение на продолжительность выполнения привычки
    """
    time = timedelta(minutes=2)

    try:
        if value['is_nice']:
            if value['associated_habit'] or value['reward']:
                raise ValidationError('У приятной привычки не может быть связанной привычки или вознаграждения')
    except KeyError:
        pass

    try:
        if value['associated_habit'] and value['reward']:
            raise ValidationError('Можно выбрать или приятную привычку или вознаграждение')
    except KeyError:
        pass

    try:
        if value['time_complete'] > time:
            raise ValidationError('Привычку можно выполнять не более 2 минут')
    except KeyError:
        pass

    try:
        if value['associated_habit']:
            if not value['associated_habit'].is_nice:
                raise ValidationError('В связанные привычки могут попадать только приятные привычки')
    except KeyError:
        pass
