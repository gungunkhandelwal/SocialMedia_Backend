from django.urls import path,include
from .views import FriendRequestViewSet, ConnectionViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'friend-requests',FriendRequestViewSet,basename='friend-request')
router.register(r'connections',ConnectionViewSet,basename='connection')

urlpatterns=[
    path('',include(router.urls)),
]