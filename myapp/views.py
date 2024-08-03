from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer

def index(request):
        print(request.user)
        return HttpResponse("This is an index page")

class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, post_id=None):
        if post_id:
            # Get details of a specific post
            post = get_object_or_404(Post, id=post_id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            # Fetch all posts
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)

    def post(self, request, post_id=None):
        if post_id:
            # Like a post
            user = request.user
            post = get_object_or_404(Post, id=post_id)

            # Check if the user has already liked the post
            if Like.objects.filter(user=user, post=post).exists():
                return Response(
                    {"detail": "Already liked"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Create a new like
            like = Like.objects.create(user=user, post=post)
            serializer = LikeSerializer(like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"detail": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST
            )
