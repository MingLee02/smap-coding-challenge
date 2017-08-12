from django.contrib import admin
from .models import Consumption, UserData


class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'area', 'tariff')


class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime', 'consumption')


admin.site.register(Consumption, ConsumptionAdmin)
admin.site.register(UserData, UserDataAdmin)