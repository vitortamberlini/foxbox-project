from django.urls import path

from cars.views import CarCreateView, CarBulkEditView

app_name = "cars"

urlpatterns = [
    path("cars/add/", CarCreateView.as_view(), name="car-create"),
    path("cars/edit/", CarBulkEditView.as_view(), name="car-bulk-edit"),
]
