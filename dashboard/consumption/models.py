from django.db import models
from django.utils import timezone


class UserData(models.Model):
    user_id = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    tariff = models.CharField(max_length=255)


class Consumption(models.Model):
	datetime = models.DateTimeField(default=timezone.now)
	consumption = models.IntegerField(default=0)