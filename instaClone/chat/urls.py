from django.urls import path
from . views import *

urlpatterns=[
    path('conversation/',ConversationListCreateView.as_view(),name='conversation'),
    path('conversation/<int:conversation_id>/message/',MessageListCreateView.as_view(),name='message')
]