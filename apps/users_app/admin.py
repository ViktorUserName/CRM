from django.contrib import admin

from apps.users_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'role')
    search_fields = ('last_name', 'first_name', 'email')
    list_filter = ('role',)
