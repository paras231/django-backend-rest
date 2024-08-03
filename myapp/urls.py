from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # get all posts
    path("posts/",views.posts, name="posts"),
    # ex: /myapp/5/
    path("<int:post_id>/", views.details, name="details"),
]