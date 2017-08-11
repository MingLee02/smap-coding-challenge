from django.contrib import admin
from .models import UserData


class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'area', 'tariff')

admin.site.register(UserData, UserDataAdmin)