import pytest

from cars.forms import CarForm
from cars.models import BrandChoices, ColorChoices


@pytest.fixture
def valid_data():
    return {
        "model": "Model 1",
        "brand": BrandChoices.BMW,
        "main_color": ColorChoices.BLUE,
        "value": 50000,
        "production_cost": 30000,
        "transportation_cost": 2000,
    }


class TestCarForm:
    @pytest.mark.parametrize(
        "model", ("", None), ids=("`model` as empty string", "`model` as `None`")
    )
    def test_invalid_model(self, valid_data, model):
        invalid_data = valid_data.copy()
        invalid_data["model"] = model

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "model" in form.errors
        assert form.errors["model"] == ["This field is required."]

    def test_invalid_brand(self, valid_data):
        invalid_data = valid_data.copy()
        invalid_data["brand"] = "Not a valid brand"

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "brand" in form.errors
        assert form.errors["brand"] == [
            "Select a valid choice. Not a valid brand is not one of the available choices."
        ]

    def test_invalid_color(self, valid_data):
        invalid_data = valid_data.copy()
        invalid_data["main_color"] = "Not a valid color"

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "main_color" in form.errors
        assert form.errors["main_color"] == [
            "Select a valid choice. Not a valid color is not one of the available choices."
        ]

    @pytest.mark.parametrize(
        "value", ("", None), ids=("`value` as empty string", "`value` as `None`")
    )
    def test_invalid_value(self, value, valid_data):
        invalid_data = valid_data.copy()
        invalid_data["value"] = value

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "value" in form.errors
        assert form.errors["value"] == ["This field is required."]

    def test_negative_value(self, valid_data):
        invalid_data = valid_data.copy()
        invalid_data["value"] = -5000

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "value" in form.errors
        assert form.errors["value"] == ["Value can't be negative."]

    @pytest.mark.parametrize(
        "production_cost",
        ("", None),
        ids=("`production_cost` as empty string", "`production_cost` as `None`"),
    )
    def test_invalid_production_cost(self, production_cost, valid_data):
        invalid_data = valid_data.copy()
        invalid_data["production_cost"] = production_cost

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "production_cost" in form.errors
        assert form.errors["production_cost"] == ["This field is required."]

    def test_negative_production_cost(self, valid_data):
        invalid_data = valid_data.copy()
        invalid_data["production_cost"] = -5000

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "production_cost" in form.errors
        assert form.errors["production_cost"] == ["Production cost can't be negative."]

    @pytest.mark.parametrize(
        "transportation_cost",
        ("", None),
        ids=(
            "`transportation_cost` as empty string",
            "`transportation_cost` as `None`",
        ),
    )
    def test_invalid_transportation_cost(self, transportation_cost, valid_data):
        invalid_data = valid_data.copy()
        invalid_data["transportation_cost"] = transportation_cost

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "transportation_cost" in form.errors
        assert form.errors["transportation_cost"] == ["This field is required."]

    def test_negative_transportation_cost(self, valid_data):
        invalid_data = valid_data.copy()
        invalid_data["transportation_cost"] = -5000

        form = CarForm(data=invalid_data)

        assert not form.is_valid()
        assert "transportation_cost" in form.errors
        assert form.errors["transportation_cost"] == [
            "Transportation cost can't be negative."
        ]
