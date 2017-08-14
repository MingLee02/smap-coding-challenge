import os

from django.conf import settings
from django.test import TestCase

from ..utils import get_directory_contents


class TestUtils(TestCase):
    def test_get_directory(self):
        """Assert default folder contents can be gotten"""
        response = get_directory_contents()
        root_path = os.path.abspath(os.path.join(settings.BASE_DIR, os.pardir))
        expected_path = os.path.join(root_path, 'data')
        expected_files = ['consumption', 'user_data.csv']

        expected_response = expected_path, expected_files
        
        self.assertEqual(response, expected_response)

    def test_get_directory_with_parameter(self):
        """Assert default folder contents can be gotten with a parameter passed"""
        response = get_directory_contents(
            directory='test_data'
        )
        root_path = os.path.abspath(os.path.join(settings.BASE_DIR, os.pardir))
        expected_url = os.path.join(root_path, 'test_data')
        expected = (expected_url, ['consumption', 'user_data.csv'])
        
        self.assertEqual(response, expected)

    def test_get_directory_with_incorrect_parameter(self):
        response = get_directory_contents(directory='fakkkkkeee')

        root_path = os.path.abspath(os.path.join(settings.BASE_DIR, os.pardir))
        expected_path = os.path.join(root_path, 'fakkkkkeee')
        
        self.assertEqual(
            response,
            (expected_path, [])
        )
