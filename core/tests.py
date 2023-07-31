import pytest
from core.models import BaseModel


class TestBaseModel:
    def test_fields(self):
        # Given: a model that inherits from BaseModel
        class MyModel(BaseModel):
            pass

        # When: we instantiate it
        model = MyModel()

        # Then: it should have an id set
        assert model.id is not None

    def test_abstract_model(self):
        # When: we instantiate BaseModel
        # Then: an error should be raised
        with pytest.raises(TypeError, match="Abstract models cannot be instantiated."):
            BaseModel()
