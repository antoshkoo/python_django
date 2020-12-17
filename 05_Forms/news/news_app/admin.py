from django.contrib import admin
from .models import *

# Register your models here.


class NewsCommentsInLine(admin.TabularInline):
    model = NewsComments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at', 'is_active']
    list_filter = ['is_active']
    inlines = [NewsCommentsInLine]

    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=1)

    def make_inactive(self, request, queryset):
        queryset.update(is_active=0)

    make_active.short_description = 'Сделать активными'
    make_inactive.short_description = 'Сделать неактивными'


@admin.register(NewsComments)
class NewsCommentsAdmin(admin.ModelAdmin):
    list_filter = ['user_name']
    list_display = ['user_name', 'short_comment', 'news']

    actions = ['delete_by_admin']

    def delete_by_admin(self, request, queryset):
        queryset.update(comment_text='Удалено администратором')

    def short_comment(self, obj):
        if len(obj.comment_text) < 15 or obj.comment_text=='Удалено администратором':
            return obj.comment_text
        else:
            return f'{obj.comment_text[:15]}...'

    delete_by_admin.short_description = 'Пометить "Удалено администратором"'
    short_comment.short_description = 'Комментарий'

