from django.contrib import admin

from apps.users_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = list_display = ('username', 'email', 'role')
    list_filter = ('role',)
