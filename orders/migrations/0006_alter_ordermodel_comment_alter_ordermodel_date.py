# Generated by Django 5.0.3 on 2024-03-23 21:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_ordermodel_comment_alter_ordermodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='comment',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 24, 0, 55, 48, 923288), null=True),
        ),
    ]
