from django.contrib import admin

from .models import *


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {
                'fields': ('name', 'description', 'count_of_employers', 'director', 'chef'),
            }),
            ('Контакты', {
                'fields': ('phone', 'country', 'city', 'street', 'house'),
                'description': 'Контактные данные',
            }),
            ('Кухня', {
                'fields': ('serves_hot_dogs', 'serves_pizza', 'serves_sushi', 'serves_burgers', 'serves_donats',
                           'serves_coffee'),
                'description': 'Тип кухни',
            }),
    )


@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('restaurant', 'first_name', 'last_name', 'age', 'sex'),
            'description': 'Основные данные'
        }),
        ('Контакты', {
            'fields': ('country', 'city', 'street', 'house', 'apartment'),
            'description': 'Контактные данные'
        }),
        ('Специализация', {
            'fields': ('seniority', 'education', 'cources'),
            'description': 'Дополнительные данные',
            'classes': ['collapse']
        })
    )