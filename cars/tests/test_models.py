from unittest import TestCase

from cars.models import Car


class TestNothing(TestCase):
    """Meaningless test just so pytest succeeds"""

    def test_true(self):
        assert True


class TestCarModel(TestCase):
    def test_fields(self):
        # Given: A car blueprint
        kwargs = {
            "model": "Model 1",
            "brand": "Brand 1",
            "main_color": "Color 1",
            "value": 50000,
            "production_cost": 30000,
            "transportation_cost": 2000,
        }

        # When: creating this object
        car = Car(**kwargs)

        # Then: All of its attributes are properly set
        assert car.model == kwargs["model"]
        assert car.brand == kwargs["brand"]
        assert car.main_color == kwargs["main_color"]
        assert car.value == kwargs["value"]
        assert car.production_cost == kwargs["production_cost"]
        assert car.transportation_cost == kwargs["transportation_cost"]
        assert (
            car.total_cost == kwargs["production_cost"] + kwargs["transportation_cost"]
        )
        assert car.id is not None
