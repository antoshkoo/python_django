from django.contrib import admin

# Register your models here.
from .models import Post, Gallery


class GalleryInline(admin.TabularInline):
    model = Gallery


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'modified', 'user']
    list_display_links = ['id', 'title']
    readonly_fields = ['modified']
    inlines = [GalleryInline]
