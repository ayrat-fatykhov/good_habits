from datetime import timedelta

from django.db import models

from config import settings


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Определяет поля для модели Habit
    """
    PERIOD_CHOICES = (
        ('1', 'ежедневно'),
        ('2', 'каждые два дня'),
        ('3', 'каждые три дня'),
        ('4', 'каждые четыре дня'),
        ('5', 'каждые пять дня'),
        ('6', 'каждые шесть дня'),
        ('7', 'еженедельно'),
    )

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_nice = models.BooleanField(default=True, verbose_name='признак приятной привычки')
    associated_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.CharField(
        max_length=1,
        choices=PERIOD_CHOICES,
        default='1',
        verbose_name='переодичность'
    )
    reward = models.CharField(max_length=100, verbose_name=' вознаграждение', **NULLABLE)
    time_complete = models.DurationField(default=timedelta(minutes=2), verbose_name='время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('pk',)
