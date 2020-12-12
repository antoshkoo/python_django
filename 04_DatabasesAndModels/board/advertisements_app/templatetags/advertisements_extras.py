from django import template
from advertisements_app.models import AdvertisementCurrency
register = template.Library()

last_currency = AdvertisementCurrency.objects.last()


@register.filter(name='usd_price')
def usd_price(value):
    return round(value / last_currency.currency, 2)


@register.simple_tag
def currency_date():
    return f'(По курсу на {last_currency.date.strftime("%d-%m-%Y")} - {round(last_currency.currency, 2)}₽)'