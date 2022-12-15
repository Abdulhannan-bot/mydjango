"""
To remder HTML web page
"""
import random
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template

HTML_STRING = """
<h1>Hello World</h1>
"""

def home_view(request, *args, **kwargs):
  """
  Take in a request (Django sends requests)
  And return an HTML response (We pick to return the response)
  """
  article_obj = Article.objects.get(id = 10)
  my_list = [11,12,13,14,15,16]
  # article_title = article_obj.title
  # article_title = article_obj.content
  article_queryset = Article.objects.all()

  # number = random.randint(19,12322)
  # country = 'united-arab-emirates'
  # youtube_link = f"""<a href="https://www.infoplease.com/countries/{country}", target = "_blank">Click Here</a>"""
  # your_number = f"""Your number  = {number}"""

  context = {
    "object_list": article_queryset,
    "object": article_obj,
    "id": article_obj.id,
    "title": article_obj.title,
    "content": article_obj.content,
  }
  H1_STRING = render_to_string('home-view.html',context = context)

  # Alternate way
  # tmpl = get_template("home-view.html")
  # tmpl_string = tmpl.render(context=context)
  # tmpl_string1 = tmpl.render(context=context)
  # tmpl_string2 = tmpl.render(context=context)

  # H1_STRING = """<h1 style="color: yellow">{id}: {title}, {content}</h1>""".format(**context)

  return HttpResponse(H1_STRING)

# def login_view(request):
#   context = {}
#   # if(request.method == 'POST'):
#     query_dict = request.POST
#     username = query_dict.get('username')
#     password = query_dict.get('password')
#     user = authenticate(request, username = username, password = password)
#     H_STRING =""
#     if user is None:
#       context['auth'] = False
#       H_STRING = render_to_string('accounts/login.html',context = context)
#       # return(request, "articles/login.html", context)
#       return HttpResponse(H_STRING)
    
#     else:
#       H_STRING = render_to_string('home-view.html',context = context)
#       # return(request, "home-view.html", context)
#       return HttpResponse(H_STRING)