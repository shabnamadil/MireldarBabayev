from django.urls import path

from .views import BlogDetailView, BlogListView

urlpatterns = [
    path(
        "blogs/",
        BlogListView.as_view(),
        name="blogs",
    ),
    path(
        "blogs/<str:slug>/",
        BlogDetailView.as_view(),
        name="blog-detail",
    ),
]
