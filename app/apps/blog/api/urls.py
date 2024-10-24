from django.urls import path

from .views import (
    BlogListAPIView,
    CommentPostAPIView,
    CommentRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name='blogs'),
    path('comment/', CommentPostAPIView.as_view(), name='comment'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-update-destroy')
]