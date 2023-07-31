import pytest
from cars.forms import CarForm


class TestCarForm:
    def test_valid_data(self, valid_car_data):
        # Given: a valid data
        # When: send this data to CarForm
        form = CarForm(data=valid_car_data)

        # Then: Data is valid
        assert form.is_valid()

    @pytest.mark.parametrize(
        "model", ("", None), ids=("`model` as empty string", "`model` as `None`")
    )
    def test_invalid_model(self, valid_car_data, model):
        # Given: a valid data with invalid model
        invalid_data = valid_car_data.copy()
        invalid_data["model"] = model

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "model" in form.errors
        assert form.errors["model"] == ["This field is required."]

    def test_invalid_brand(self, valid_car_data):
        # Given: a valid data with invalid brand
        invalid_data = valid_car_data.copy()
        invalid_data["brand"] = "Invalid brand"

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "brand" in form.errors
        assert form.errors["brand"] == ["Value 'Invalid brand' is not a valid choice."]

    def test_invalid_color(self, valid_car_data):
        # Given: a valid data with invalid color
        invalid_data = valid_car_data.copy()
        invalid_data["main_color"] = "Invalid color"

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "main_color" in form.errors
        assert form.errors["main_color"] == [
            "Value 'Invalid color' is not a valid choice."
        ]

    @pytest.mark.parametrize(
        "value", ("", None), ids=("`value` as empty string", "`value` as `None`")
    )
    def test_invalid_value(self, value, valid_car_data):
        # Given: a valid data with invalid value
        invalid_data = valid_car_data.copy()
        invalid_data["value"] = value

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "value" in form.errors
        assert form.errors["value"] == ["This field is required."]

    def test_negative_value(self, valid_car_data):
        # Given: a valid data with invalid value
        invalid_data = valid_car_data.copy()
        invalid_data["value"] = -5000

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "value" in form.errors
        assert form.errors["value"] == [
            "Ensure this value is greater than or equal to 0."
        ]

    @pytest.mark.parametrize(
        "production_cost",
        ("", None),
        ids=("`production_cost` as empty string", "`production_cost` as `None`"),
    )
    def test_invalid_production_cost(self, production_cost, valid_car_data):
        # Given: a valid data with invalid production_cost
        invalid_data = valid_car_data.copy()
        invalid_data["production_cost"] = production_cost

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "production_cost" in form.errors
        assert form.errors["production_cost"] == ["This field is required."]

    def test_negative_production_cost(self, valid_car_data):
        # Given: a valid data with invalid production cost
        invalid_data = valid_car_data.copy()
        invalid_data["production_cost"] = -5000

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "production_cost" in form.errors
        assert form.errors["production_cost"] == [
            "Ensure this value is greater than or equal to 0."
        ]

    @pytest.mark.parametrize(
        "transportation_cost",
        ("", None),
        ids=(
            "`transportation_cost` as empty string",
            "`transportation_cost` as `None`",
        ),
    )
    def test_invalid_transportation_cost(self, transportation_cost, valid_car_data):
        # Given: a valid data with invalid transportation_cost
        invalid_data = valid_car_data.copy()
        invalid_data["transportation_cost"] = transportation_cost

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "transportation_cost" in form.errors
        assert form.errors["transportation_cost"] == ["This field is required."]

    def test_negative_transportation_cost(self, valid_car_data):
        # Given: a valid data with invalid transportation_cost
        invalid_data = valid_car_data.copy()
        invalid_data["transportation_cost"] = -5000

        # When: send this data to CarForm
        form = CarForm(data=invalid_data)

        # Then: data is invalid
        assert not form.is_valid()

        # And: error message is shown
        assert "transportation_cost" in form.errors
        assert form.errors["transportation_cost"] == [
            "Ensure this value is greater than or equal to 0."
        ]
