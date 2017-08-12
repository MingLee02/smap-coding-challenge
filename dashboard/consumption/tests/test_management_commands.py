from django.core.management import call_command
from django.test import TestCase


class TestImport(TestCase):
    def test_handle(self):
        call_command('import')