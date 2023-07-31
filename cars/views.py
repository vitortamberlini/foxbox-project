import json

from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from cars.forms import CarForm, CarFormSet
from cars.models import Car, BrandChoices, ColorChoices


class CarListView(ListView):
    model = Car
    context_object_name = "cars"
    template_name = "cars/car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["BRAND_CHOICES"] = json.dumps(
            {choice[0]: choice[1] for choice in BrandChoices.choices}
        )
        context["COLOR_CHOICES"] = json.dumps(
            {choice[0]: choice[1] for choice in ColorChoices.choices}
        )

        return context


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "cars/car_form2.html"
    success_url = reverse_lazy("cars:car-bulk-edit")


class CarBulkEditView(View):
    template_name = "cars/car_bulk_edit.html"
    success_url = reverse_lazy("cars:car-bulk-edit")
    form_class = CarForm

    def get_formset(self):
        return modelformset_factory(Car, form=self.form_class, extra=0)

    def get(self, request):
        formset = CarFormSet(queryset=Car.objects.all())
        return render(request, self.template_name, {"formset": formset})

    def post(self, request):
        formset = CarFormSet(request.POST, queryset=Car.objects.all())
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {"formset": formset})
