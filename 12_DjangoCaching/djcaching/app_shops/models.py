from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Shop name'))

    def __str__(self):
        return self.name

    def get_goods_sales(self):
        return self.sale_set.filter(shop_id=self.id)

    def get_goods_no_sales(self):
        return self.goods.filter(sales__sale_price=None)


class Good(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='goods')
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0, verbose_name=_('Price'))

    def __str__(self):
        return f'{self.name} ({self.shop.name})'


class Sale(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='sales')
    sale_price = models.FloatField(default=0, verbose_name=_('Sale price'))

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
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    price_order = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user, self.good.name, self.price_order, self.date.strftime('%d.%m.%Y')
