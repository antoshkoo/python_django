import requests
from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime

from advertisements_app.models import AdvertisementCurrency


class Command(BaseCommand):
    help = 'Получение курса валют'

    def handle(self, *args, **kwargs):
        today = timezone.now().strftime('%Y-%m-%d')
        if AdvertisementCurrency.objects.filter(date=today).exists():
            return f'Курс был обновлен {today}'
        else:
            responce = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            if responce.status_code == 200:
                data = responce.json()
                usd_currency = data['Valute']['USD']['Value']
                AdvertisementCurrency.objects.create(
                    date=timezone.now(),
                    currency_name='USD',
                    currency=usd_currency,
                )
                return f'Курс обновлен {today}'
            else:
                return f'Ошибка парсинга'
