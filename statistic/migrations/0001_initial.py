# Generated by Django 5.0.3 on 2024-03-27 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClickersModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(blank=True, max_length=1000, verbose_name='User Agent')),
                ('session_id', models.CharField(blank=True, max_length=1000, verbose_name='ID сессии')),
                ('computer_name', models.CharField(blank=True, max_length=1000, verbose_name='Имя компьютера')),
                ('processor_info', models.CharField(blank=True, max_length=1000, verbose_name='Информация о процессоре')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 27, 15, 59, 50, 862261), null=True, verbose_name='Дата')),
            ],
        ),
    ]