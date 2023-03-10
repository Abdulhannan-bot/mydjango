from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
import random
from django.db.models import Q
from django.conf import settings

from .utils import slugify_instance_title


User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
  def search(self,query=None):
    if query is None or query == "":
      return self.none()
    lookup = Q(title__icontains=query) | Q(content__icontains=query)
    return self.filter(lookup)

class ArticleManager(models.Manager):
  def get_queryset(self):
    return ArticleQuerySet(self.model, using = self.db)

  def search(self,query=None):
    return self.get_queryset().search(query = query)



# Create your models here.

class Article(models.Model):
  user = models.ForeignKey(User, blank = True, null = True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=120)
  slug = models.SlugField(unique = True, blank = True, null = True)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add = True)
  updated = models.DateTimeField(auto_now = True)
  publish = models.DateTimeField(auto_now = False, null = True, blank = True) #null = True blank = True auto_now_add = False, auto_now = False, default = timezone.now

  objects = ArticleManager()

  # def save(self, *args, **kwargs):
    
  #   if(self.slug is None):
  #     slugify_instance_title(self, save=False)
  #   super().save(*args,**kwargs)
  def get_absolute_url(self):
    # return f'articles/{self.slug}/'
    return reverse("article-detail", kwargs = {"slug":self.slug})

  def __str__(self):
    return str(self.title)

def article_pre_save(sender, instance, *args, **kwargs):
  print('pre-save')
  if instance.slug is None:
    slugify_instance_title(instance,save = False)
  
pre_save.connect(article_pre_save, sender = Article)

def article_post_save(sender, instance, created, *args, **kwargs):
  print('post-save')
  if created:
    slugify_instance_title(instance,save = True)

post_save.connect(article_post_save, sender = Article)