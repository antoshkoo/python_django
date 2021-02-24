from django.contrib import admin


from app_catalog.models import Book, Author


@admin.register(Book, Author)
class ShopAdmin(admin.ModelAdmin):
    pass
