from django.contrib import admin

from .models import Recipe
from .models import RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
  model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
  model = Recipe
  inlines = [RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)

# Register your models here.