import pytest

from cars.models import Car


@pytest.fixture
def car_kwargs():
    return {
        "model": "Model 1",
        "brand": "Brand 1",
        "main_color": "Color 1",
        "value": 50000,
        "production_cost": 30000,
        "transportation_cost": 2000,
    }


class TestCarModel:
    def test_fields(self, car_kwargs):
        # Given: A car blueprint
        # When: creating this object
        car = Car(**car_kwargs)

        # Then: All of its attributes are properly set
        assert car.model == car_kwargs["model"]
        assert car.brand == car_kwargs["brand"]
        assert car.main_color == car_kwargs["main_color"]
        assert car.value == car_kwargs["value"]
        assert car.production_cost == car_kwargs["production_cost"]
        assert car.transportation_cost == car_kwargs["transportation_cost"]
        assert (
            car.total_cost
            == car_kwargs["production_cost"] + car_kwargs["transportation_cost"]
        )

    def test_total_cost(self, car_kwargs):
        # Given: a car blueprint
        # When: creating this object
        car = Car(**car_kwargs)

        # Then: the total cost should be the sum of production cost and transportation cost
        assert car.total_cost == car.transportation_cost + car.production_cost
