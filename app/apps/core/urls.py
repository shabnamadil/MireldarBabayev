from django.urls import path

from .views import (
    ContactPageView,
    AboutUsPageView,
    HomePageView,
    FaqListView
)

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutUsPageView.as_view(), name='about'),
    path('faq/', FaqListView.as_view(), name='faq'),
    path('', HomePageView.as_view(), name='home')
]