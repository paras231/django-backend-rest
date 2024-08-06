from django.urls import path
from .views import PostView , IndexView , LoginView

urlpatterns = [ 
    path('', IndexView.as_view(), name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('posts/', PostView.as_view(),name='posts'),
    path('posts/<int:post_id>/', PostView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/like/', PostView.as_view(), name='like_post'),
]
