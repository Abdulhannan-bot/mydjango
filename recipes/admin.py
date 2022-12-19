from django.contrib.auth import get_user_model
from django.contrib import admin

# Register your models here.

User = get_user_model

from .models import RecipeIngredient, Recipe

# admin.site.register(RecipeIngredient)

class RecipeIngredientInline(admin.StackedInline):
  model = RecipeIngredient
  extra = 0
  readonly_fields = ['quantity_as_float', 'to_mks', 'to_imperial']
  # fields = ['name', 'quantity', 'unit', 'directions']

class RecipeAdmin(admin.ModelAdmin):
  inlines = [RecipeIngredientInline]
  list_diplay = ['name', 'user']
  readonly_fields = ['timestamp', 'updated']
  raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)


