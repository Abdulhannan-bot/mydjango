from django.urls import path
from articles import views


app_name = 'articles'

urlpatterns = [
    path('articles/', views.article_search_view, name="search"),
    path('create-articles/', views.article_create_view, name = "article-create"),
    path('articles/<slug:slug>/', views.article_detail_view, name = "article-detail"), #path('articles/<int:id>/'
]
