import pytest
from cars.models import Car


@pytest.mark.django_db
class TestCarModel:
    def test_fields(self, valid_car_data):
        # Given: A car blueprint
        # When: creating this object
        car = Car(**valid_car_data)

        # Then: All of its attributes are properly set
        assert car.model == valid_car_data["model"]
        assert car.brand == valid_car_data["brand"]
        assert car.main_color == valid_car_data["main_color"]
        assert car.value == valid_car_data["value"]
        assert car.production_cost == valid_car_data["production_cost"]
        assert car.transportation_cost == valid_car_data["transportation_cost"]
        assert (
            car.total_cost
            == valid_car_data["production_cost"] + valid_car_data["transportation_cost"]
        )

    def test_total_cost(self, valid_car_data):
        # Given: a car blueprint
        # When: creating this object
        car = Car(**valid_car_data)

        # Then: the total cost should be the sum of production cost and transportation cost
        assert car.total_cost == car.transportation_cost + car.production_cost
