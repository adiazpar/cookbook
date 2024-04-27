from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# ---------------------- INGREDIENT MODEL ----------------------- #
class Ingredient(models.Model):
    title = models.CharField(max_length=200, default='')

    # Define default String to return the name for representing the Model object:
    def __str__(self):
        return self.title


# ---------------- INGREDIENT & QUANTITY MODEL ------------------ #
class IngredientSet(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    quantity = models.CharField(max_length=20, blank=True)
    unit = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "{0} {1} {2}".format(self.quantity, self.unit, self.ingredient)


# ------------------------ RECIPE MODEL ------------------------- #
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=500, default='')
    ingredients = models.ManyToManyField(IngredientSet, blank=True)

    # Define default String to return the name for representing the Model object:
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])
