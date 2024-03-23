# Generated by Django 5.0.3 on 2024-03-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_site', '0004_datasitemodel_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='MastersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='media', verbose_name='Аватар')),
                ('name', models.CharField(max_length=255, verbose_name='Имя мастера')),
                ('post', models.CharField(max_length=255, verbose_name='Должность мастера')),
                ('description', models.TextField(verbose_name='Описание мастера')),
                ('sort', models.IntegerField(blank=True, default=0, verbose_name='Индекс сортировки')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
    ]