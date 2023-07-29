from django.test import TestCase
from django.urls import reverse


class TestCarListView(TestCase):
    def test_view_exists(self):
        url = reverse("cars:car-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
