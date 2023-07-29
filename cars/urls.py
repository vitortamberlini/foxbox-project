from django.urls import path, include
from cars.views import CarListView

app_name = "cars"

urlpatterns = [
    path("", CarListView.as_view(), name="car-list"),
]
