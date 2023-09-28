from django.db import models

from users.models import User
from utils.utilites import NULLABLE


class Habit(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    place = models.CharField(max_length=50, **NULLABLE,  verbose_name='Место')
    time = models.TimeField(auto_now_add=True, **NULLABLE,  verbose_name='Время')
    action = models.CharField(max_length=150, **NULLABLE,  verbose_name='Действие')

    is_nice = models.BooleanField(default=False, **NULLABLE,  verbose_name='признак приятной привычки')
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE)

    periodicity = models.SmallIntegerField(**NULLABLE,  verbose_name='Периодичность в днях')
    reward = models.CharField(max_length=150, **NULLABLE,  verbose_name='Награда')
    duration = models.SmallIntegerField(**NULLABLE,  verbose_name='Продолжительность в секундах')

    is_public = models.BooleanField(default=False, **NULLABLE,  verbose_name='признак публичной привычки')

    def __str__(self):
        return f'Habit: author={self.author}, place={self.place}, time={self.time}, action={self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['-created_date']