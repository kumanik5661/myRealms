from .views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),

    path('allPosts', allPosts, name='allPosts'),
    
    path('allPosts/post/<int:post_id>/',viewPost, name='view_post' ),
]

        