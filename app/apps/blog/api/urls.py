from django.urls import path

from .views import (
    BlogListAPIView,
    CommentListPostAPIView,
    CommentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('blogs/', BlogListAPIView.as_view()),
    path('comment/', CommentListPostAPIView.as_view(), name='comment'),
    path(
        'comment/<int:pk>/',
        CommentRetrieveUpdateDestroyAPIView.as_view(),
        name='comment-update-destroy',
    ),
]
