from django.urls import path

from .views import (
    NewsletterCreateAPIView,
    ContactPostAPIView
)


urlpatterns = [
    path('newsletter/', NewsletterCreateAPIView.as_view(), name='newsletter'),
    path('contact/', ContactPostAPIView.as_view(), name='contact')
]