from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe

# Create your views here.
def home(request):
    # http response
    return render(request, 'recipes\\pages\\home.html', context={
        'recipes': [make_recipe() for _ in range(6)]})

def recipe(request, id):
    # http response
    return render(request, 'recipes\\pages\\recipe_view.html', context={
        'recipe': make_recipe(),
        'is_detail': True})




