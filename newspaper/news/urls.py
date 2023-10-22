from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.list_create_articles, name='articles'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)