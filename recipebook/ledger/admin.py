from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient, Profile, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
  model = RecipeIngredient

class RecipeImagineInline(admin.TabularInline):
  model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
  model = Recipe
  inlines = [RecipeIngredientInline, RecipeImagineInline]
  search_fields = ('name', 'author', 'created_on', 'updated_on')
  list_display = ('name', 'author', 'created_on', 'updated_on')

  fieldsets = {
    ('Details', {
      'fields': [
        ('name', 'author')
      ]
    })
  }

class IngredientAdmin(admin.ModelAdmin):
  model = Ingredient

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

# Register your models here.