from django import forms
from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "model",
            "brand",
            "main_color",
            "value",
            "production_cost",
            "transportation_cost",
        ]

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
