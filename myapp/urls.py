from django.urls import path
from .views import PostView

urlpatterns = [ 
    path('/', PostView.as_view({'get': 'index'}), name='index'),
    path('posts/', PostView.as_view(), name='posts'),
    path('posts/<int:post_id>/', PostView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/like/', PostView.as_view(), name='like_post'),
]
