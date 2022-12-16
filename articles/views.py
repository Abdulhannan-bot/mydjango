from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.http import Http404
from django.db.models import Q

# Create your views here.

from .models import Article


def article_search_view(request):
  query = request.GET.get('q')

  # print(f'ans = {query_dict}')
  # try:
  #   query = int(query_dict.get("q"))
  # except:
  #   query = None
  # qs = Article.objects.all()
  # article_obj = None
  # if query is not None:
  #   lookups = Q(title__icontains = query) #| Q(content__icontains = query)
    # qs = Article.objects.filter(lookups)
  qs = Article.objects.search(query = query)
  print(qs)
    # article_obj = Article.objects.get(id = query)
  context = {
    # "object": article_obj,
    "object_list": qs #ArticleManager.search(Article,query)
  }
  return render(request, "articles/search.html",context=context)

#@csrf_exempt
@login_required
def article_create_view(request):

  form = ArticleForm(request.POST or None)
  print(dir(form))
  context = {
    "form": form,
  }
  
  if (form.is_valid()):
    article_object = form.save()
    context['form'] = ArticleForm()
    context['object'] = article_object
    context['created'] = True


  # form = ArticleForm(request.POST or None)
  # print(dir(form))
  # context = {
  #   "form": form,
  # }
  
  # if (form.is_valid()):
  #   title = form.cleaned_data.get('title')
  #   # title = form.clean_title()

  #   content = form.cleaned_data.get('content')
  #   # content = form.clean_content()

  #   article_object = Article.objects.create(title = title, content = content)
  #   context['title'] = title
  #   context['content'] = content 
  #   context['object'] = article_object
  #   context['created'] = True


  # form = ArticleForm()
  # print(dir(form))
  # context = {
  #   "form": form,
  # }
  # if(request.method == 'POST'):
  #   # query_dict = request.POST
  #   # title = query_dict.get('title')
  #   # content = query_dict.get('content')

  #   form = ArticleForm(request.POST)
  #   context['form'] = form
  #   if (form.is_valid()):
  #     # title = form.cleaned_data.get('title')
  #     title = form.clean_title()

  #     # content = form.cleaned_data.get('content')
  #     content = form.clean_content()

  #     article_object = Article.objects.create(title = title, content = content)
  #     context['title'] = title
  #     context['content'] = content 
  #     context['object'] = article_object
  #     context['created'] = True


  return render(request, "articles/create.html",context=context)

def article_detail_view(request, slug = None):
  article_obj = None
  if slug is not None:
    try:
      article_obj = Article.objects.get(slug = slug)
    except Article.DoesNotExist:
      raise Http404
    except Article.MultipleObjectsReturned:
      article_obj = Article.objects.get(slug = slug).first()
    except:
      raise Http404
  context = {
    "object": article_obj,
  }


  return render(request, "articles/detail.html", context=context)


def login_view(request):
  
  context = {}
  # if(request.method == 'POST'):
    
  #   query_dict = request.POST
  #   username = query_dict.get('username')
  #   password = query_dict.get('password')
  #   user = authenticate(request, username = username, password = password)
  #   print(user)
  #   if (user is None):
  #     context['error'] = "Invalid username or password"
  #     return render(request, "accounts/login.html", context = context)
  #   login(request, user)
  #   return redirect('/')
  if(request.method == 'POST'):
    form = AuthenticationForm(request, data=request.POST)
    if(form.is_valid()):
      user = form.get_user()
      login(request, user)
      return redirect('/')
  else:
    form = AuthenticationForm(request)
  context['form'] = form
  return render(request, "accounts/login.html", context = context)

def logout_view(request):
  if(request.method == 'POST'):
    logout(request)
    return redirect('/login')
  return render(request, "accounts/logout.html",{})

def register_view(request):
  form = UserCreationForm(request.POST or None)
  context = {"form": form}
  if(form.is_valid()):
    user_obj = form.save()
    return redirect('/login')
    context = {
      "form": form
    }
  return render(request,'accounts/register.html',context)
