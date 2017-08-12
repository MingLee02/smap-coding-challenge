from django.test import TestCase

from ..utils import get_directory_contents


class TestUtils(TestCase):
    def test_get_directory(self):
        """Assert default folder contents can be gotten"""
        response = get_directory_contents()
        expected_path = '/Users/mlee/Sites/smap-coding-challenge/data'
        expected_files = ['consumption', 'user_data.csv']

        expected_response = expected_path, expected_files
        
        self.assertEqual(response, expected_response)

    def test_get_directory_with_parameter(self):
        """Assert default folder contents can be gotten with a parameter passed"""
        response = get_directory_contents(
            directory='test_data'
        )

        expected_url = '/Users/mlee/Sites/smap-coding-challenge/test_data'
        expected = (expected_url, ['test_data_two', 'user_data.csv'])
        
        self.assertEqual(response, expected)

    def test_get_directory_with_incorrect_parameter(self):
        response = get_directory_contents(directory='fakkkkkeee')
        
        self.assertEqual(
            response,
            ('/Users/mlee/Sites/smap-coding-challenge/fakkkkkeee', None)
        )
