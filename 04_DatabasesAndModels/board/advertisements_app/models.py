import datetime

from django.db import models
from django.utils import timezone


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, db_index=True, verbose_name='Заголовок')
    description = models.TextField(default=None, verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    ended_at = models.DateTimeField(default=(timezone.now() + datetime.timedelta(days=30)),
                                    verbose_name='Дата окончания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)
    type = models.ForeignKey('AdvertisementType', default=None, null=True, blank=True, related_name='type',
                             on_delete=models.CASCADE, verbose_name='Тип')
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, blank=True, related_name='status',
                               on_delete=models.CASCADE, verbose_name='Статус')
    author = models.ForeignKey('AdvertisementAuthor', default=None, blank=False, related_name='author',
                               on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey('AdvertisementCategory', default=None, null=True, blank=True, related_name='category',
                                 on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']

    def views_counter(self):
        advertisement = Advertisement.objects.get(id=self.pk)
        advertisement.views_count += 1
        advertisement.save()
        return advertisement.views_count


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    phone = models.IntegerField(unique=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_author'


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_type'


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_status'


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_category'


class AdvertisementCurrency(models.Model):
    date = models.DateTimeField(verbose_name='Дата обновления')
    currency_name = models.CharField(max_length=5, verbose_name='Валюта')
    currency = models.FloatField(verbose_name='Курс')

    def __str__(self):
        return self.currency

    class Meta:
        db_table = 'advertisement_currency'
