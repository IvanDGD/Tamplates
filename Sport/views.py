import random

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "SportMain.html")
def football(request):
    return render(request, "SportFootball.html")
def hockey(request):
    return render(request, "SportHockey.html")
def basketball(request):
    return render(request, "SportBasketball.html")
