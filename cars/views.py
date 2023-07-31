from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from cars.forms import CarForm, CarFormSet
from cars.models import Car


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "cars/car_form.html"
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
            for form in formset:
                if form.has_changed():
                    print("Changed!")
                    formset.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {"formset": formset})
