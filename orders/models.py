from datetime import datetime

import pytz as pytz
from django.db import models


class OrderModel(models.Model):

    status_choices = [
        ('T', 'Треш'),
        ('P', 'Перезвонить'),
        ('A', 'Подтвержден'),
        ('R', 'Отклонён'),
        ('N', 'Новый'),
    ]

    name = models.CharField(max_length=20, blank=True, verbose_name=f'Имя клиента')

    phone = models.CharField(max_length=12, blank=False, verbose_name=f'Телефон клиента')

    id_client = models.CharField(max_length=20, blank=False, verbose_name=f'Идентификатор клиента')

    status = models.CharField(max_length=1, choices=status_choices, db_index=True, default='N', verbose_name=f'Статус')

    date = models.DateTimeField(blank=True, null=True, default=datetime.now(), verbose_name=f'Дата')

    comment = models.CharField(max_length=1255, blank=True, null=True, verbose_name=f'Комментарий')

    url = models.CharField(max_length=1255, blank=True, null=True, verbose_name=f'UTM метка')

    ip = models.CharField(max_length=255, blank=True, null=True, verbose_name=f'IP адрес')

    class Meta:
        verbose_name = f'Заказ'
        verbose_name_plural = f'Заказы'
