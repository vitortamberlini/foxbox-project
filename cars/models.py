from django.db import models

from core.models import BaseModel


class BrandChoices(models.TextChoices):
    BMW = "bmw", "BMW"
    FORD = "ford", "Ford"


class ColorChoices(models.TextChoices):
    RED = "red", "Red"
    BLUE = "blue", "Blue"


class Car(BaseModel):
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=50, choices=BrandChoices.choices)
    main_color = models.CharField(max_length=50, choices=ColorChoices.choices)
    value = models.IntegerField()
    production_cost = models.IntegerField()
    transportation_cost = models.IntegerField()

    @property
    def total_cost(self):
        return self.production_cost + self.transportation_cost
