from django.urls import path
from .views import CurrencyExchangeRate

urlpatterns = [
    path('show_rates/', CurrencyExchangeRate.as_view())
]
