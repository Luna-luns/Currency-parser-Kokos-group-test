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

        for key, value in currencies_dict.items():
            if not Currency.objects.filter(char_code=value['CharCode']).exists():
                Currency.objects.create(
                    char_code=value['CharCode'],
                    name=value['Name']
                )

            CurrencyExchangeRates.objects.create(
                currency=Currency.objects.get(
                    char_code=value['CharCode']),
                date=date.today(),
                value=float(value['Value'])
            )
