from django.db import models
from django.conf import settings
from .validators import validate_unit_of_measure
from .utils import number_str_to_float
import pint
from django.urls import reverse
# Create your models here.

class Recipe(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  name = models.CharField(max_length=220)
  description = models.TextField(blank=True, null=True)
  directions  = models.TextField(blank=True, null=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def get_absolute_url(self):
    return reverse("recipes:detail", kwargs={"id": self.id})

  def get_edit_url(self):
    return reverse("recipes:update", kwargs={"id": self.id})

  def get_delete_url(self):
    return reverse("recipes:delete", kwargs={"id": self.id})

  def ingredients_children(self):
    return self.recipeingredient_set.all()

  def __str__(self):
    return str(self.name)

class RecipeIngredient(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  name = models.CharField(max_length=220)
  description = models.TextField(blank=True, null=True)
  quantity = models.CharField(max_length=50)
  quantity_as_float = models.FloatField(blank=True, null=True)
  unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
  directions  = models.TextField(blank=True, null=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def get_absolute_url():
    return self.recipes.get_absolute_url()

  def save(self, *args, **kwargs):
    qty = self.quantity
    qty_as_float, qty_as_float_succsss = number_str_to_float(qty)
    if(qty_as_float_succsss):
      self.quantity_as_float = qty_as_float
    else:
      self.quantity_as_float = None
    super().save(*args, **kwargs)

  def convert_to_system(self, system="mks"):
    if self.quantity_as_float is None:
      return None
    ureg = pint.UnitRegistry(system=system)
    measurement = self.quantity_as_float * ureg[self.unit]
    print(measurement)
    return measurement
  

  def to_mks(self):
    # meters, kilograms, seconds
    measurement = self.convert_to_system(system="mks")
    print(measurement)
    return measurement.to_base_units()

  def to_imperial(self):
    # miles, pounds, seconds
    measurement = self.convert_to_system(system="imperial")
    print(measurement)
    return measurement.to_base_units()

  def __str__(self):
    return str(self.name)
