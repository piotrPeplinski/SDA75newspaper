from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.ListCreateArticles.as_view(), name='articles'),
    path('users/', views.ListUsers.as_view(), name='users'),
    path('articles/<int:pk>/',
         views.ArticleDetail.as_view(), name='article_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
