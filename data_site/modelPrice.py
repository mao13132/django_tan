from django.db import models


class PriceModel(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name=f'Название')

    description = models.TextField(blank=False, verbose_name=f'Описание')

    price = models.IntegerField(verbose_name=f'Стоимость')

    class Meta:
        verbose_name = f'Прайс'
        verbose_name_plural = f'Прайс'

    def __str__(self):
        return f'{self.name} - {self.price} ₽'
