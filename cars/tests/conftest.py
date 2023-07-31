from django.test import Client
import pytest
from django.urls import reverse
from cars.models import BrandChoices, ColorChoices


@pytest.fixture(scope="session")
def client():
    return Client()


@pytest.fixture(scope="session")
def car_bulk_edit_endpoint():
    return reverse("cars:car-bulk-edit")


@pytest.fixture(scope="session")
def car_create_endpoint():
    return reverse("cars:car-create")


@pytest.fixture
def valid_car_data():
    return {
        "model": "Model 1",
        "brand": BrandChoices.BMW,
        "main_color": ColorChoices.BLUE,
        "value": 50000,
        "production_cost": 30000,
        "transportation_cost": 2000,
    }
