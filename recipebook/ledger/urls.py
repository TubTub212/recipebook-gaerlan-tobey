from django.urls import path

from .views import recipeList, recipe1, recipe2

urlpatterns = [
    path('recipes/list', recipeList, name='recipe-list'),
    path('recipe/1', recipe1, name='recipe_1'),
    path('recipe/2', recipe2, name='recipe_2')
]

app_name = "ledger"