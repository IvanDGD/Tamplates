from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("text/", views.text_format, name="text_format")
]