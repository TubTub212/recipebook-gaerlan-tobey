from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe, Ingredient

class RecipeListView(ListView):
    model = Recipe
    recipes = Recipe.objects.all()
    template_name = 'recipe-list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'


