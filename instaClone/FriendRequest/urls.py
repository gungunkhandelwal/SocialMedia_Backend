from django.urls import path
from .views import *

urlpatterns=[
    path('',FriendRequestView.as_view(),name="friend_request")
]