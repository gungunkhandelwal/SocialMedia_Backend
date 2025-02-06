from django.urls import path
from . views import *

urlpatterns = [
    path('', PostListCreateApi.as_view(), name='post-list-create'),
    path('<int:id>/', PostRetrieveDeleteAPI.as_view(), name='post-retrieve-delete'),
    path('likes/',LikeCountCreateView.as_view(),name='likes' ),
    path('comments/',CommentListCreateView.as_view(),name='comments'),
    path('profile/',ProfileView.as_view(),name='user-profile')
]
