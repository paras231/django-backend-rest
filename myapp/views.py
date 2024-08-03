from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post
from .models import Post
# Create your views here.

# get all posts
def index(request):
    return HttpResponse("This is an index page")


def posts(request):
    posts =  Post.objects.all() 
    data = list(posts.values())  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)


#  get details of a specific post
def details(request,post_id):
    print(post_id)
    response =  'Your are looking at this post details page %s'
    return HttpResponse(response % post_id)
    