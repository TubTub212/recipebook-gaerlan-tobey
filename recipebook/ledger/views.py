from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Recipe, Ingredient, RecipeImage
from .forms import RecipeForm, RecipeImageForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe-list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    ingredients = Ingredient.objects.filter(recipe__recipe__name="recipe.name")
    template_name = 'recipe.html'

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'add-recipe.html'
    form_class = RecipeForm

class RecipeImageCreateView(CreateView):
    model = RecipeImage
    template_name = 'add-image.html'
    form_class = RecipeImageForm
