# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------

from django.db import models


class MastersModel(models.Model):
    avatar = models.ImageField(upload_to='media', verbose_name='Аватар')
    name = models.CharField(max_length=255, blank=False, verbose_name='Имя мастера')
    post = models.CharField(max_length=255, blank=False, verbose_name='Должность мастера')
    description = models.TextField(blank=False, verbose_name=f'Описание мастера')
    sort = models.IntegerField(blank=True, default=0, verbose_name=f'Индекс сортировки')

    def __str__(self):
        return f'{self.name} - {self.post}'

    class Meta:
        verbose_name = f'Мастер'
        verbose_name_plural = f'Мастера'

