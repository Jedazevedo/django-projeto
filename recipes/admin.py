from django.contrib import admin
from .models import Category, Recipe

# PRIMEIRA FORMA DE REGISTRAR UMA CATEGORIA
class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)


# SEGUNDA FORMA DE IMPORTAR REGISTRAR UMA CATEGORIA
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
