from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

# Register your models here.

# admin.site.site_header = 'News Admin'
# admin.site.unregister(Group)


class NewsCommentsInLine(admin.TabularInline):
    model = NewsComments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at', 'is_active']
    list_display_links = ['id', 'name']
    list_editable = ['is_active']
    list_filter = ['is_active', 'tags', 'created_at']
    inlines = [NewsCommentsInLine]
    fields = ['name', 'body', ('created_at', 'updated_at'), 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    save_on_top = True

    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=1)
    make_active.short_description = 'Сделать активными'

    def make_inactive(self, request, queryset):
        queryset.update(is_active=0)
    make_inactive.short_description = 'Сделать неактивными'


@admin.register(NewsComments)
class NewsCommentsAdmin(admin.ModelAdmin):
    list_filter = ['user_name']
    list_display = ['user_name', 'short_comment', 'news']

    actions = ['delete_by_admin']

    def delete_by_admin(self, request, queryset):
        queryset.update(comment_text='Удалено администратором')

    def short_comment(self, obj):
        if len(obj.comment_text) < 15 or obj.comment_text == 'Удалено администратором':
            return obj.comment_text
        else:
            return f'{obj.comment_text[:15]}...'

    delete_by_admin.short_description = 'Пометить "Удалено администратором"'
    short_comment.short_description = 'Комментарий'


@admin.register(NewsTags)
class NewsTagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']