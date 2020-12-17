from django.contrib import admin
from .models import *

# Register your models here.


class NewsCommentsInLine(admin.TabularInline):
    model = NewsComments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    inlines = [NewsCommentsInLine]


@admin.register(NewsComments)
class NewsCommentsAdmin(admin.ModelAdmin):
    list_filter = ['user_name']
    list_display = ['user_name', 'comment_text']
