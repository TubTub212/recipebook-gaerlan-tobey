from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[self.id])
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(null=True, max_length=50)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.id])

class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

class RecipeImage(models.Model):
    image = models.ImageField(null=False, upload_to='images/')
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE, related_name='image')

    def get_absolute_url(self):
        return reverse('ledger:images', args=[str(self.recipe.pk)])
    
    def __str__(self):
        return f'{self.recipe.name}: url({self.image}) - {self.description}'