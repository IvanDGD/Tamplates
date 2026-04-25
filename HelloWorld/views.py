import random

from django.shortcuts import render

# Create your views here.

def helloen(request):
    return render(request, "hello-world.html", {"welcome": "Hello, World!"})
