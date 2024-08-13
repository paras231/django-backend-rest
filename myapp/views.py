from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post, Like , CustomUser
from .serializers import PostSerializer, LikeSerializer , UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate

class IndexView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return HttpResponse("This is an index page")

class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

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

class UserView(APIView):
    def post(self, request):
        action = request.data.get('action')

        if action == 'create':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif action == 'login':
            email = request.data.get('username')
            
            password = request.data.get('password')
            print(request.data.get('password'))
            if not email or not password:
                return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(request, email=email, password=password)
            if user is not None:
                # Optionally, you might want to use a token-based authentication system
                # Here you can return a success message or a user-related data
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)