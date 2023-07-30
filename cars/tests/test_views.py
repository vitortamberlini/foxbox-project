from django.test import TestCase
from django.urls import reverse


class TestCarListView(TestCase):
    def setUp(self):
        self.url = reverse("cars:car-list")

    def test_view_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class TestCarCreateView(TestCase):
    def setUp(self):
        self.url = reverse("cars:car-create")

    def test_view_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
