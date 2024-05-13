from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from currency.models import CurrencyExchangeRates
from rest_framework.renderers import JSONRenderer


class CurrencyExchangeRate(APIView):
    renderer_classes = [JSONRenderer]

    @action(detail=False, methods=['get'])
    def get_currency(self, request, *args, **kwargs):
        queryset = CurrencyExchangeRates.objects.all()
        rates_data = [{"currency": rate.currency.char_code, "value": rate.value} for rate in queryset]
        return Response(rates_data)
