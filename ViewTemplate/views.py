import random

from django.shortcuts import render

# Create your views here.

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname} is {self.age} years old"

def index(request):
    context = {}
    context["welcome_text"] = "Welcome to the world of Django Templates"
    context["html_tag"] = '<h3 style="color: red;">HTML tag</h3>'
    context['value_int'] = 100
    context['value_float'] = 3.14
    context["value_bool"] = False

    context["list"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    context["dict"] = {"name": "Alex", "surname": "Smith", "age": 30}
    context["person"] = Person("Alex", "Smith", 30)
    context["random_value"] = random.randint(-100, 100)
    context["empty_list"] = []

    return render(request, "index.html", context = context)

def text_format(request):
    return render(request, "text-format.html", {"list" : [i for i in range(0, 10)]})