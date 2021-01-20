from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from app_users.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'user_balance', 'is_staff']
    inlines = [ProfileInline]

    def user_balance(self, obj):
        return obj.profile.balance


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
