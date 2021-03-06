from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Shop name'))

    def __str__(self):
        return self.name


@receiver(post_save, sender=Shop)
def create_shop(sender, instance, created, **kwargs):
    if created:
        cache.delete(make_template_fragment_key('main_shops_cache'))


@receiver(post_save, sender=Shop)
def save_shop(sender, instance, **kwargs):
    cache.delete(make_template_fragment_key('main_shops_cache'))


class Good(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='goods')
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0, verbose_name=_('Price'))

    class Meta:
        unique_together = ('shop', 'name')

    def __str__(self):
        return f'{self.name} ({self.shop.name})'


class Sale(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='sales')
    sale_price = models.FloatField(default=0, verbose_name=_('Sale price'))

    class Meta:
        unique_together = ('shop', 'good')

    def __str__(self):
        return f'{self.good.name} - {self.good.price} ({self.sale_price})'


class Promotion(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='promotions')
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return f'{self.shop.name} - ({self.title})'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    price_order = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))

    def __str__(self):
        time = self.date.strftime('%d.%m.%Y')
        return f'{self.user}, {self.good.name}, {self.price_order} - {time}'

    def total_cost(self):
        return self.price_order * self.quantity
