from django.urls import path

from .views import (
    ContactPageView,
    AboutUsPageView
)

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutUsPageView.as_view(), name='about')
]