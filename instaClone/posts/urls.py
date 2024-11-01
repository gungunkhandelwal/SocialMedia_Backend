from django.urls import path
from . views import *

urlpatterns=[
    path('',PostListCreateApi.as_view(),name='post'),
    path('posts/<int:id>/',PostRetrieveDeleteAPI.as_view(),name='post-delete-update'),
]

