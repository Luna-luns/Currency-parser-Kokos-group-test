# Generated by Django 5.0.6 on 2024-05-13 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_rename_currency_exchange_rates_currencyexchangerates'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Валюта', 'verbose_name_plural': 'Валюты'},
        ),
        migrations.AlterModelOptions(
            name='currencyexchangerates',
            options={'verbose_name': 'Курс валюты', 'verbose_name_plural': 'Курсы валют'},
        ),
    ]
