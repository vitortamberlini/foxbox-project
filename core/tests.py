from unittest import TestCase

import pytest

from core.models import BaseModel


class TestBaseModel(TestCase):
    def test_fields(self):
        class MyModel(BaseModel):
            pass

        model = MyModel()

        assert model.id is not None

    def test_abstract_model(self):
        with pytest.raises(TypeError, match="Abstract models cannot be instantiated."):
            BaseModel()
