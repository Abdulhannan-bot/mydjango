from django.contrib.auth import get_user_model
from django.test import TestCase
import pint
from django.core.exceptions import ValidationError
# Create your tests here.

from .models import RecipeIngredient, Recipe
User = get_user_model()

class UserTestCase(TestCase):
  def setUp(self):
    self.user_a =  User.objects.create_user('abd',password='ahm123')

  def test_user_pw(self):
    checked = self.user_a.check_password('ahm123')
    self.assertTrue(checked)


class RecipeTestCase(TestCase):
  def setUp(self):
    self.user_a = User.objects.create_user('abd',password='ahm123')
    self.recipe_a = Recipe.objects.create(
      name = "Grilled Chicken",
      user = self.user_a
    )
    self.recipe_b = Recipe.objects.create(
      name = "Grilled Chicken Tacos",
      user = self.user_a
    )
    self.recipe_ingredient_a = RecipeIngredient.objects.create(
      recipe = self.recipe_a,
      name = "Chicken",
      quantity = "2",
      unit = "kg"
    )

  def user_recipe_count(self):
    qs = User.objects.all()
    self.assertEqual(qs.count(), 1)

  def test_user_recipe_reverse_count(self):
    user = self.user_a
    qs = Recipe.objects.all()
    self.assertEqual(qs.count(),2)

  def test_user_recipe_forward_count(self):
    user = self.user_a
    qs = Recipe.objects.filter(user = user)
    print(f'the query set = {qs}')
    self.assertEqual(qs.count(),2)

  def test_recipe_ingredients_reverse_count(self):
    recipe = self.recipe_a
    qs = RecipeIngredient.objects.filter(recipe = recipe)
    self.assertEqual(qs.count(),1)

  # def test_user_two_level_relations(self):
  #   user = self.user_a
  #   qs = RecipeIngredient.objects.filter(recipe__user = user)
  #   self.assertEqual(qs.count(),1)

  # def test_user_two_level_reverse_relations(self):
  #   user = self.user_a
  #   recipe_ingredient_ids = user.recipe_set.all().values_list('sdfsdf', flat=True)
  #   self.assertEqual(recipe_ingredient_ids.count(),1)
  
  def test_unit_measurement(self):
    invalid_unit = 'nada'
    with self.assertRaises(ValidationError)
    ingredients = RecipeIngredient(
      recipe = self.recipe_a,
      name = "New",
      quantity = 5,
      unit = invalid_unit
    )
    ingredients.full_clean()