from django import forms

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    fields = ['name', 'description', 'directions']

  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    for field in self.fields:
      new_data = {
        "placeholder": f'Recipe {str(field)}',
        "class": "form-control",
      }
      self.fields[str(field)].widget.attrs.update(new_data)
    self.fields['description'].widget.attrs.update({'rows':2})


class RecipeIngredientForm(forms.ModelForm):
  class Meta:
    model = RecipeIngredient
    fields = ['name', 'quantity', 'unit']