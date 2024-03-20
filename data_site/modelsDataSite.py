from django.db import models


class DataSiteModel(models.Model):
    brand_name = models.CharField(max_length=255, blank=False, null=False, verbose_name=f'Бренд')

    phone = models.CharField(max_length=12, blank=False, null=False, verbose_name=f'Номер телефона')

    title = models.CharField(max_length=255, blank=False, null=False, verbose_name=f'Заголовок сайта')

    instagram = models.CharField(max_length=255, blank=True, null=True, verbose_name=f'Инстаграм')

    description = models.TextField(blank=True, null=True, verbose_name=f'Описание для SEO')

    keywords = models.TextField(blank=True, null=True, verbose_name=f'Ключевые слова для SEO')

    og_description = models.CharField(max_length=255, blank=False, null=False, verbose_name=f'Подзаголовок')

    address = models.TextField(blank=False, null=False, verbose_name=f'Адрес')

    class Meta:
        verbose_name = f'Настройка'
        verbose_name_plural = f'Главные настройки'

    def __str__(self):
        return f'Мои настройки'

    def save(self, *args, **kwargs):
        count = DataSiteModel.objects.count()

        if count >= 1:
            if not self.pk and DataSiteModel.objects.exists():

                try:
                    one_pk = DataSiteModel.objects.first().id

                    DataSiteModel.objects.filter(pk=one_pk).update(
                        address=self.address,
                        brand_name=self.brand_name, phone=self.phone,
                        title=self.title,
                        instagram=self.instagram,
                        description=self.description,
                        keywords=self.keywords,
                        og_description=self.og_description
                    )

                except Exception as es:
                    print(f'Ошибка при обновление записи промпта "{es}"')

                    return False

                return True
            else:
                DataSiteModel.objects.filter(pk=self.pk).update(
                    address=self.address,
                    brand_name=self.brand_name,
                    phone=self.phone, title=self.title,
                    instagram=self.instagram,
                    description=self.description,
                    keywords=self.keywords,
                    og_description=self.og_description
                )

        else:
            return super(DataSiteModel, self).save(*args, **kwargs)
