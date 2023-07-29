import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Base Model
    - Sets the ID field to UUID and the created fields
    """

    id = models.UUIDField(
        db_index=True, default=uuid.uuid4, editable=False, primary_key=True
    )

    class Meta:
        abstract = True
