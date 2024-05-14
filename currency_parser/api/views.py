from rest_framework.response import Response
from rest_framework.views import APIView
from currency.models import CurrencyExchangeRates


class CurrencyExchangeRate(APIView):

    def get(self, request):
        queryset = CurrencyExchangeRates.objects.all()
        rates_data = [{"currency": rate.currency.char_code, "value": rate.value} for rate in queryset]
        return Response(rates_data)
