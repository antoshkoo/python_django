from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'modified', 'user']
    list_display_links = ['id', 'title']
    readonly_fields = ['pub_date', 'modified']
