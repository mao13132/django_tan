from datetime import datetime

from django.db import models


class OrderModel(models.Model):
    name = models.CharField(max_length=20, blank=True, verbose_name=f'Имя клиента')

    phone = models.CharField(max_length=12, blank=False, verbose_name=f'Телефон клиента')

    id_client = models.CharField(max_length=20, blank=False, verbose_name=f'Идентификатор клиента')

    date = models.DateTimeField(blank=True, null=True, default=datetime.now())

    def __str__(self):
        return f'Имя: {self.name}   ---   Телефон: {self.phone}   ---   ' \
               f'Дата: {self.date.strftime("%Y-%m-%d %H:%M:%S")}   ---   ID: {self.id_client}'

    class Meta:
        verbose_name = f'Заказ'
        verbose_name_plural = f'Заказы'
