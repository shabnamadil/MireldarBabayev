from django.urls import path

from .views import LoginPageView, RegisterPageView, logout_view

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_view, name="logout"),
]
