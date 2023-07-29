from django.views.generic import ListView

from cars.models import Car


# Create your views here.
class CarListView(ListView):
    model = Car
    template_name = "cars/car_list.html"
