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

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}. {self.description}"

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

    return render(request, "./first_example/index.html", context = context)

def text_format(request):
    return render(request, "./first_example/text-format.html", {"list" : [i for i in range(0, 10)]})

def contacts(request):
    persons = [
        Person("Alex", 30, "Smith"),
        Person("John", 25, "Doe"),
        Person("Jane", 28, "Doe")
    ]
    return render(request, "second_example/contacts.html", {"persons": persons})

def products(request):
    products = [
        Product("Tomato", 100, "The freshest tomato in the world"),
        Product("Banana", 2, "Just banana"),
        Product("PC", 1000, "OHHHH MY PC")
    ]
    return render(request, "products.html", {"products": products})

def style(request):
    return render(request, "second_example/main_page.css")