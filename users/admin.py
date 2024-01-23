from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'country')
    list_filter = ('id', 'email', 'first_name', 'last_name', 'country')
    list_display_links = ('id', 'email', 'first_name', 'last_name', 'country')
