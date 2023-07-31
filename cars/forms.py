from django import forms
from django.forms import modelformset_factory

from cars.models import Car, BrandChoices, ColorChoices


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ["id"]

    brand = forms.CharField(
        max_length=50, widget=forms.Select(choices=BrandChoices.choices)
    )
    main_color = forms.CharField(
        max_length=50, widget=forms.Select(choices=ColorChoices.choices)
    )
    value = forms.IntegerField(min_value=0, step_size=100)
    production_cost = forms.IntegerField(min_value=0, step_size=100)
    transportation_cost = forms.IntegerField(min_value=0, step_size=100)

    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value < 0:
            raise forms.ValidationError("Value can't be negative.")
        return value

    def clean_production_cost(self):
        production_cost = self.cleaned_data.get("production_cost")
        if production_cost < 0:
            raise forms.ValidationError("Production cost can't be negative.")
        return production_cost

    def clean_transportation_cost(self):
        transportation_cost = self.cleaned_data.get("transportation_cost")
        if transportation_cost < 0:
            raise forms.ValidationError("Transportation cost can't be negative.")
        return transportation_cost


CarFormSet = modelformset_factory(Car, form=CarForm, extra=0)
