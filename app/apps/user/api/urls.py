from django.urls import path

from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    LogoutAPIView,
    RegisterAPIView,
    UserMeAPIView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register_api'),
    path(
        'token/',
        CustomTokenObtainPairView.as_view(),
        name='custom_token_obtain_pair',
    ),
    path(
        'token/refresh/',
        CustomTokenRefreshView.as_view(),
        name='token_refresh',
    ),
    path('user/me/', UserMeAPIView.as_view(), name='user_me_api'),
    path('logout/', LogoutAPIView.as_view(), name='logout_api'),
]
