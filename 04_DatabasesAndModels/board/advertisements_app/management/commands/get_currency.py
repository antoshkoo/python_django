import datetime
import requests
from django.core.management.base import BaseCommand
from django.utils import timezone

from advertisements_app.models import AdvertisementCurrency


class Command(BaseCommand):
    help = 'Получение курса валют'

    def handle(self, *args, **kwargs):
        responce = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        if responce.status_code == 200:
            data = responce.json()
            usd_currency = data['Valute']['USD']['Value']
        else:
            return f'Ошибка парсинга'
        obj, created = AdvertisementCurrency.objects.get_or_create(
            date=timezone.now(),
            defaults={'currency_name': 'USD',
                      'currency': usd_currency},
        )
