from django.urls import path

from .views import (
    ContactPostAPIView,
    NewsletterCreateAPIView,
)

urlpatterns = [
    path(
        "newsletter/",
        NewsletterCreateAPIView.as_view(),
        name="newsletter",
    ),
    path("contact/", ContactPostAPIView.as_view()),
]
