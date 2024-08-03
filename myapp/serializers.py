

from rest_framework import serializers
from .models import Post,Author,Like


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nest the AuthorSerializer
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'author']  # specify fields you want to include


class LikeSerializer(serializers.ModelSerializer):
      class Meta:
          model = Like
          fields = ['user', 'post', 'created_at']
