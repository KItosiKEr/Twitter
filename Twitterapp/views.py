from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .seriallizers import PostSeriallizer

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSeriallizer



# Create your views here.
