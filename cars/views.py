from django.views.generic import ListView, CreateView

from cars.forms import CarForm
from cars.models import Car


class CarListView(ListView):
    model = Car
    context_object_name = "cars"
    template_name = "cars/car_list.html"


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "cars/car_form.html"
    success_url = "/cars/"
