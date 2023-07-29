from cars.models import Car
from django.contrib import admin


class MyModelAdmin(admin.ModelAdmin):
    list_filter = ("model",)
    search_fields = ("model",)


admin.site.register(Car, MyModelAdmin)
