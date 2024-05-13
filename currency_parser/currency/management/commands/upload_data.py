import requests
from datetime import date

from django.core.management import BaseCommand

from currency.models import Currency, CurrencyExchangeRates


class Command(BaseCommand):
    help = 'Собирает и загружает курсы валют в базу данных из json.'

    def handle(self, *args, **options):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        json_data = response.json()
        currencies_dict = json_data['Valute']

        rates = [
            CurrencyExchangeRates(
                currency=Currency.objects.get(
                    Currency,
                    char_code=value['CharCode'],
                    name=value['Name']
                ),
                date=date.today(),
                value=value['Value']
            )
            for key, value in currencies_dict.items()
        ]

        CurrencyExchangeRates.objects.bulk_create(rates)
