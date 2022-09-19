from django.shortcuts import render, HttpResponse
from . import models
recipes = [
    {
        'author': 'Ky',
        'title': 'meatball sub',
        'directions': 'combine all ingredients',
        'date_posted': 'May 19 2022'
    },
    {
        'author': 'Ky',
        'title': 'VN sub',
        'directions': 'combine all ingredients',
        'date_posted': 'May 09 2022'
    },
    {
        'author': 'Ky',
        'title': 'USA sub',
        'directions': 'combine all ingredients',
        'date_posted': 'May 29 2022'
    },
]
# Create your views here.


def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)


def about(request):
    return render(request, "recipes/about.html", {'title': 'About us page'})