import random

from django.shortcuts import render

# Create your views here.

recipes = [
        {"name": "Goulash",
         "ingredients": ["beef", "onion", "paprika", "potatoes", "carrots", "garlic", "tomato paste"]},
        {"name": "Dumplings", "ingredients": ["flour", "egg", "milk", "salt"]},
        {"name": "Pancakes", "ingredients": ["flour", "milk", "egg", "sugar", "butter"]},
        {"name": "Omelette", "ingredients": ["eggs", "milk", "cheese", "salt", "pepper"]},
        {"name": "Tomato Soup", "ingredients": ["tomatoes", "onion", "garlic", "vegetable broth", "cream"]}
    ]

def index(request):
    recipe_name = request.GET.get("recipe")

    if recipe_name:
        recipe = next((r for r in recipes if r["name"] == recipe_name), None)
        return render(request, "recipesGET.html", {"recipe": recipe})

    return render(request, "recipesList.html", {"recipes": recipes})