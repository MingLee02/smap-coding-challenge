from django.core.management import call_command
from django.test import TestCase


class TestImport(TestCase):
    def test_handle_pass_invalid_parameter(self):
        args = ['ssd']
        response = call_command('import', *args)
        self.assertEqual(response, None)