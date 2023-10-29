from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class ListCreateArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return [permissions.IsAdminUser() if self.request.method == 'GET' else permissions.AllowAny()]
