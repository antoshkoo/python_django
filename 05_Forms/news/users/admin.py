from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Unregister the provided model admin
from .models import Profile

admin.site.unregister(User)
# Register out own model admin, based on the default UserAdmin


class UserProfileInLine(admin.TabularInline):
    model = Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'last_name', 'first_name', 'is_verified']
    inlines = [UserProfileInLine]

    def is_verified(self, object):
        return 'Да' if object.profile.is_verified else 'Нет'

    is_verified.short_description = ("Статус верификации")

    def get_queryset(self, request):
        return super(CustomUserAdmin, self).get_queryset(request).select_related('profile')