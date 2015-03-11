from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):

    fieldsets = (
        ('User', {'fields': ('username', 'password')}),
        ('Persona Info', {
         'fields': ('first_name', 'last_name', 'email', 'avatar')}),
        ('Social Networks', {
         'fields': (
            'facebook', 'twitter', 'googleplus', 'instagram', 'website')}),
        ('Permissions', {
         'fields': (
            'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

admin.site.register(User, UserAdmin)
