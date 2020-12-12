import datetime
import requests
from django.core.management.base import BaseCommand
from django.utils import timezone

from advertisements_app.models import AdvertisementCurrency


class Command(BaseCommand):
    help = 'Получение курса валют'

    def handle(self, *args, **kwargs):
        last_currency_update = AdvertisementCurrency.objects.last()
        last_currency = last_currency_update.date.strftime("%d-%m-%Y")
        now = datetime.datetime.today().strftime("%d-%m-%Y")
        if now == last_currency:
            return f'Курс на сегодня уже обновлен'
        else:
            responce = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            if responce.status_code == 200:
                data = responce.json()
                usd_currency = data['Valute']['USD']['Value']
                today_currency = AdvertisementCurrency(date=timezone.now(), currency_name='USD', currency=usd_currency)
                today_currency.save()
            else:
                return f'Ошибка парсинга'
