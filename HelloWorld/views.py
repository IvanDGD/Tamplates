import random

from django.shortcuts import render

# Create your views here.

def hello(request):
    context = {}
    context["welcome"] = ""
    path = request.path
    match(path):
        case "/welcome/":
            context["welcome"] = "Hello, World!"
        case "/welcome/fr/":
            context["welcome"] = "Bonjour le monde!"
        case "/welcome/de/":
            context["welcome"] = "Hallo, Welt!"
        case "/welcome/es/":
            context["welcome"] = "¡Hola Mundo!"
    return render(request, "hello-world.html", context = context)
