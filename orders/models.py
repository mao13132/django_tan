from datetime import datetime

import pytz as pytz
from django.db import models


class OrderModel(models.Model):
    name = models.CharField(max_length=20, blank=True, verbose_name=f'Имя клиента')

    phone = models.CharField(max_length=12, blank=False, verbose_name=f'Телефон клиента')

    id_client = models.CharField(max_length=20, blank=False, verbose_name=f'Идентификатор клиента')

    date = models.DateTimeField(blank=True, null=True, default=datetime.now())

    comment = models.CharField(max_length=1255, blank=True, null=True, verbose_name=f'Комментарий')

    class Meta:
        verbose_name = f'Заказ'
        verbose_name_plural = f'Заказы'
