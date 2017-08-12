from django.core.management import call_command
from django.conf import settings
from django.test import TestCase

from consumption.models import Consumption, UserData


class TestImport(TestCase):
    def test_handle(self):
        args = 'test_data'
        call_command('import', args)

        user_one_id = '3011'
        user_two_id = '3029'
        user_data = UserData.objects.all()

        self.assertEqual(len(user_data), 2)
        self.assertEqual(user_data[0].user_id, user_one_id)
        self.assertEqual(user_data[1].user_id, user_two_id)

        consumption_one_consumption = 3
        consumption_two_consumption = 2 
        consumption_data = Consumption.objects.all()

        self.assertEqual(len(consumption_data), 2)
        self.assertEqual(consumption_data[0].consumption, consumption_one_consumption)
        self.assertEqual(consumption_data[1].consumption, consumption_two_consumption)
        self.assertEqual(consumption_data[0].user.user_id, user_one_id)
        self.assertEqual(consumption_data[1].user.user_id, user_two_id)