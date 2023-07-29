from django.db import models

from core.models import BaseModel


class Car(BaseModel):
    BRAND_CHOICES = [
        ("bmw", "BMW"),
        ("ford", "Ford"),
    ]

    COLOR_CHOICES = [
        ("red", "Red"),
        ("blue", "Blue"),
    ]

    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    main_color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    value = models.IntegerField()
    production_cost = models.IntegerField()
    transportation_cost = models.IntegerField()

    @property
    def total_cost(self):
        return self.production_cost + self.transportation_cost
