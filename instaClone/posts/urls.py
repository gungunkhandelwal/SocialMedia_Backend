from django.urls import path
from . views import *

urlpatterns=[
    path('',PostApi.as_view(),name='post'),
]

