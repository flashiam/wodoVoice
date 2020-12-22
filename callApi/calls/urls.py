from django.urls import path
from . import views

urlpatterns = [
    path("custCall", views.getCalls, name="custCall"),
]