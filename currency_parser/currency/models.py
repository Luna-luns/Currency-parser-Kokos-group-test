from django.db import models


class Currency(models.Model):
    char_code = models.CharField(
        verbose_name='Код ISO валюты',
        max_length=50,
        unique=True
    )
    name = models.CharField(
        verbose_name='Название валюты',
        max_length=250
    )

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name


class CurrencyExchangeRates(models.Model):
    currency = models.ForeignKey(
        Currency,
        verbose_name='Валюта',
        on_delete=models.CASCADE
    )
    date = models.DateField(
        verbose_name='Дата сбора данных',
        auto_now_add=True)
    value = models.FloatField(
        verbose_name='Курс валюты'
    )

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
        constraints = [
            models.UniqueConstraint(
                fields=['currency', 'date'],
                name='unique_currency_date'
            )
        ]

    def __str__(self):
        return f'{self.currency} - {self.value}'
