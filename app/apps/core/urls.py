from django.urls import path

from .views import (
    ContactPageView,
    AboutUsPageView,
    HomePageView
)

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutUsPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')
]