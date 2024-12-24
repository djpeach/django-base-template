from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.sessions.models import Session

from apps.accounts.models import User


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    pass
