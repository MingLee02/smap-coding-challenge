from django.db import models


class UserData(models.Model):
    user_id = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    tariff = models.CharField(max_length=255)