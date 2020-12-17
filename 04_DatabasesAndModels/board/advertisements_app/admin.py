from django.contrib import admin

# Register your models here.
from advertisements_app.models import *


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    search_fields = ['description']


@admin.register(AdvertisementAuthor)
class AdvertisementAuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']

#
# @admin.register(AdvertisementType)
# class AdvertisementTypeAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(AdvertisementStatus)
# class AdvertisementStatusAdmin(admin.ModelAdmin):
#     pass


@admin.register(AdvertisementCategory)
class AdvertisementCategoryAdmin(admin.ModelAdmin):
    pass
