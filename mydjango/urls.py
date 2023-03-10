"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views
from .views import home_view
from django.urls import include

urlpatterns = [
    path('', home_view), # home, index, root
    path('pantry/recipes/', include('recipes.urls')),
    path('articles/', views.article_search_view, name="search"),
    path('create-articles/', views.article_create_view, name = "article-create"),
    path('articles/<slug:slug>/', views.article_detail_view, name = "article-detail"), #path('articles/<int:id>/'
    path('admin/', admin.site.urls),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.register_view)
]
