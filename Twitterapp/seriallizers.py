from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSeriallizer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
