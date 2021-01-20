from django.contrib import admin

from app_shops.models import Shop, Good, Sale, Promotion, Order


@admin.register(Shop, Good, Sale, Promotion, Order)
class ShopAdmin(admin.ModelAdmin):
    pass