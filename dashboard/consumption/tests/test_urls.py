from django.test import TestCase
from django.urls import reverse

from .factories import UserDataFactory


class TestSummaryUrl(TestCase):
	def test_url(self):
		url = reverse('summary')

		self.assertEqual(url, '/')


class TestDetailUrl(TestCase):
	def test_url(self):
		user = UserDataFactory.create()
		url = reverse('detail', kwargs={'user_id': user.user_id})
		expected_url = '/detail/{}'.format(user.user_id)

		self.assertEqual(url, expected_url)