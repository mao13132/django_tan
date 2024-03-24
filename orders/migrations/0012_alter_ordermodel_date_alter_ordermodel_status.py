# Generated by Django 5.0.3 on 2024-03-23 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_ordermodel_date_alter_ordermodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 24, 1, 14, 9, 180456), null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(choices=[('T', 'Треш'), ('P', 'Перезвонить'), ('A', 'Подтвержден'), ('R', 'Отклонён')], db_index=True, default='R', max_length=1),
        ),
    ]
