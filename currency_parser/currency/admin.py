from django.contrib.admin import ModelAdmin, register
from .models import Currency, CurrencyExchangeRates


@register(Currency)
class CurrencyAdmin(ModelAdmin):
    """Отображение в админ панели валюты."""
    list_display = ('char_code', 'name')
    list_filter = ('char_code',)


@register(CurrencyExchangeRates)
class Currency_exchange_ratesAdmin(ModelAdmin):
    """Отображение в админ панели курсов валют."""
    list_display = ('currency', 'date', 'value')
    list_filter = ('currency',)
    search_fields = ('date',)
