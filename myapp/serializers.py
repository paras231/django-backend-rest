

from rest_framework import serializers
from .models import Post,Author,Like,CustomUser


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


class UserSerializer(serializers.ModelSerializer):
      class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'is_staff', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
            return user