from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="helloworld"),
    path("fr/", views.hello, name="helloworld"),
    path("de/", views.hello, name="helloworld"),
    path("es/", views.hello, name="helloworld"),
]