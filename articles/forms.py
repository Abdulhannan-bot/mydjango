from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ['title','content']

  def clean(self):
    data = self.cleaned_data
    title = data.get('title')
    qs = Article.objects.filter(title__icontains = title)
    if(qs.exists()):
      self.add_error('title',f'{title} is already taken')
    return data



class ArticleFormOld(forms.Form):
  title = forms.CharField()
  content = forms.CharField()

  # def clean_title(self):
  #   cleaned_data = self.cleaned_data
  #   title = cleaned_data.get('title')
  #   if(title.lower().strip() == 'david copperfield'):
  #     raise forms.ValidationError('This title is taken')
  #   return title

  # def clean_content(self):
  #   cleaned_data = self.cleaned_data
  #   content = cleaned_data.get('content')
  #   return content

  def clean_data(self):
    cleaned_data = self.cleaned_data
    title = cleaned_data.get('title')
    content = cleaned_data.get('content')
    if(title.lower().strip() == 'david copperfield'):
      # self.add_error('title','This title is taken')
      raise forms.ValidationError('This title is taken')
    return cleaned_data