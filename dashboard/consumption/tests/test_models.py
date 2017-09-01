from django.test import TestCase

from .factories import ConsumptionFactory, UserDataFactory
from ..models import Consumption, UserData


class TestUserData(TestCase):
    def test_str(self):
        name = 12
        userData = UserDataFactory.build(user_id=name)
        self.assertEqual(userData.user_id, name)


class TestConsumption(TestCase):
    def test_str(self):
        userData = UserDataFactory.create()
        consumption = ConsumptionFactory.build(user=userData)
        self.assertEqual(consumption.user.user_id, userData.user_id)