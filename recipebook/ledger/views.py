from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe, Ingredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe-list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    ingredients = Ingredient.objects.filter(recipe__recipe__name="recipe.name")
    template_name = 'recipe.html'


