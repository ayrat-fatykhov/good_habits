from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Определяет поля для модели 'Пользватель'. Реализуют возможность взаимодействия с пользователем через email.
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активность', **NULLABLE)
    last_login = models.DateTimeField(auto_now=True, verbose_name="последний вход", **NULLABLE)

    telegram = models.CharField(max_length=20, verbose_name='телеграм', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
