from django.apps import AppConfig


class StatisticConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'statistic'

    verbose_name = f'Статистика сайта'