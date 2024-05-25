from rest_framework import serializers

from habits.models import Habit
from habits.validators import habit_validators


class HabitSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность. Для модели Habit
    """
    class Meta:
        model = Habit
        fields = '__all__'

    validators = [
        habit_validators,
    ]
