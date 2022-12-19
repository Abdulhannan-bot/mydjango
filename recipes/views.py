from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import modelformset_factory
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm
from django.urls import reverse

# Create your views here.

@login_required
def recipe_list_view(request, id=None):
  qs = Recipe.objects.filter(user = request.user)
  context = {
    "object_list": qs,
  }
  return render(request, 'recipes/list.html', context)

@login_required
def recipe_detail_view(request, id=None):
  obj = get_object_or_404(Recipe, id=id, user = request.user)
  context = {
    "object":obj,
  }
  return render(request, 'recipes/detail.html', context)

@login_required
def recipe_create_view(request):
  form_recipe = RecipeForm(request.POST or None)
  context = {
    "form_recipe": form_recipe,
  }
  if form_recipe.is_valid():
    obj = form_recipe.save(commit = False)
    obj.user = request.user
    obj.save()
    return redirect(obj.get_absolute_url())
  return render(request, 'recipes/create-update.html', context)

@login_required
def recipe_update_view(request, id=None):
  obj = get_object_or_404(Recipe, id=id, user = request.user)
  form_recipe = RecipeForm(request.POST or None, instance = obj)
  # form_ingredients = RecipeIngredientForm(request.POST or None)
  qs = obj.recipeingredient_set.all()
  ingredients_formset = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=0)
  formset = ingredients_formset(request.POST or None, queryset = qs)
  context = {
    "form_recipe": form_recipe,
    # "form_ingredients": form_ingredients,
    "formset": formset,
    "object":obj,
  }
  if(request.method =='POST'):
    print(request.POST)
  if all([form_recipe.is_valid(), formset.is_valid()]):
    parent = form_recipe.save(commit = False)
    parent.save()
    for form in formset:
      child = form.save(commit = False)
      # if(child.recipe is None):
      child.recipe = parent
      child.save()
    # child = form_ingredients.save(commit = False)
    # child.recipe = parent
    # child.save()
    context['message'] = 'Data Saved'
    # return redirect(obj.get_absolute_url())
  return render(request, 'recipes/create-update.html', context)


@login_required
def recipe_delete_view(request, id = None):
  obj = get_object_or_404(Recipe, id=id, user=request.user)
  print(obj)
  if(request.method=='POST'):
    print('Method is Post')
    obj.delete()
    success_url = reverse('recipes:list')
    return redirect(success_url)
  context = {
    "object": obj
  }
  print('Method is not post')
  return render(request, 'recipes/delete.html', context)


@login_required
def ingredient_delete_view(request, id = None, parent_id = None):
  obj = get_object_or_404(RecipeIngredient, id=id, recipe__id=parent_id, recipe__user = request.user)
  if(request.method == 'POST'):
    obj.delete()
    success_url = reverse('recipes:detail', kwargs={"id": parent_id} )
    return redirect(success_url)
  context = {
    "object": obj
  }
  return render(request,'recipes/delete.html', context)
