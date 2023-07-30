import pytest

from cars.models import Car


@pytest.mark.django_db
class TestCarListView:
    def test_view_exists(self, client, car_list_endpoint):
        response = client.get(car_list_endpoint)
        assert response.status_code == 200


@pytest.mark.django_db
class TestCarCreateView:
    def test_view_exists(self, client, car_create_endpoint):
        response = client.get(car_create_endpoint)
        assert response.status_code == 200

    def test_car_create_view_post(
        self, client, car_create_endpoint, car_list_endpoint, valid_car_data
    ):
        response = client.post(car_create_endpoint, data=valid_car_data)

        assert response.status_code == 302
        assert response.url == car_list_endpoint

        assert Car.objects.count() == 1
        new_car = Car.objects.first()
        assert new_car.brand == valid_car_data["brand"]
        assert new_car.model == valid_car_data["model"]
        assert new_car.value == valid_car_data["value"]
        assert new_car.production_cost == valid_car_data["production_cost"]
        assert new_car.transportation_cost == valid_car_data["transportation_cost"]
