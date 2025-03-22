from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    # http response
    return render(request, 'recipes\\pages\\home.html', context={
        'recipes': recipes})#[make_recipe() for _ in range(3)]})

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id = category_id).order_by('-id')
    # http response
    return render(request, 'recipes\\pages\\home.html', context={
        'recipes': recipes})#[make_recipe() for _ in range(3)]})

def recipe(request, id):
    # http response
    return render(request, 'recipes\\pages\\recipe_view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True})




