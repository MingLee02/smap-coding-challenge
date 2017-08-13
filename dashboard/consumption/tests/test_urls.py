from django.test import TestCase
from django.urls import reverse


class TestSummaryUrl(TestCase):
	def test_url(self):
		url = reverse('summary')

		self.assertEqual(url, '/')