from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Shop name'))

    def __str__(self):
        return self.name


class Good(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='goods')
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0, verbose_name=_('price'))

    def __str__(self):
        return f'{self.name} ({self.shop_id.name})'


class Sale(models.Model):
    good_id = models.OneToOneField(Good, on_delete=models.CASCADE)
    sale_price = models.FloatField(default=0, verbose_name=_('sale_price'))

    def __str__(self):
        return f'{self.good_id.name} - ({self.sale_price})'


class Promotion(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='promotions')
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return f'{self.shop_id.name} - ({self.title})'


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    good_id = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='orders')
