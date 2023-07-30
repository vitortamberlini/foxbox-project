from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cars.urls", namespace="cars")),
    re_path(r"^.*$", RedirectView.as_view(pattern_name="cars:car-list")),
]
