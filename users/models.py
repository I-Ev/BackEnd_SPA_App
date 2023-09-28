from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.utilites import NULLABLE


class User(AbstractUser):
    username = None

    telegram_name = models.CharField(max_length=50, unique=True, verbose_name='телеграм аккаунт')
    email = models.EmailField(unique=True, verbose_name='Email', **NULLABLE)
    chat_id = models.IntegerField(default=0, verbose_name='ID чата', **NULLABLE)
    update_id = models.PositiveBigIntegerField(default=0, **NULLABLE, verbose_name='ID последнего сообщения')

    USERNAME_FIELD = "telegram_name"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'User: {self.telegram_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
