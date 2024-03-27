from datetime import datetime

from django.db import models


class ClickersModule(models.Model):
    user_agent = models.CharField(max_length=1000, blank=True, verbose_name=f'User Agent')
    utm = models.CharField(max_length=10000, blank=True, verbose_name=f'utm метки')
    ip = models.CharField(max_length=255, blank=True, null=True, verbose_name=f'IP адрес')
    session_id = models.CharField(max_length=1000, blank=True, verbose_name=f'ID сессии')
    computer_name = models.CharField(max_length=1000, blank=True, verbose_name=f'Имя компьютера')
    processor_info = models.CharField(max_length=1000, blank=True, verbose_name=f'Информация о процессоре')
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name=f'Дата')

    class Meta:
        verbose_name = 'Клик'
        verbose_name_plural = 'Клики'
