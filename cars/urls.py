from django.urls import path

from cars.views import CarListView, CarCreateView

app_name = "cars"

urlpatterns = [
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/add/", CarCreateView.as_view(), name="car-create"),
]
