from django.contrib import admin

from .models import Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
  model = Recipe
  inlines = [RecipeIngredient]

admin.site.register(Recipe)
admin.site.register(RecipeIngredient)

   
# Register your models here.
