from django.test import TestCase

from ..utils import get_directory_contents


class TestUtils(TestCase):
    def test_get_directory(self):
        """Assert default folder contents can be gotten"""
        response = get_directory_contents()
        expected = ['consumption', 'user_data.csv']
        
        self.assertEqual(response, expected)

    def test_get_directory_with_parameter(self):
        """Assert default folder contents can be gotten with a parameter passed"""
        response = get_directory_contents('dashboard/consumption/tests/test_data')
        expected = ['user_data.csv']
        
        self.assertEqual(response, expected)

    def test_get_directory_with_incorrect_parameter(self):
        response = get_directory_contents('fakkkkkeee')
        
        self.assertEqual(response, None)
