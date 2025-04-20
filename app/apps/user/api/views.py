from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .serializers import RegisterSerializer, UserInfoSerializer

User = get_user_model()


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class UserMeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserInfoSerializer(request.user)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Extract refresh token
        refresh_token = response.data.get('refresh')
        access_token = response.data.get('access')

        # Create new response with only access token
        res = Response(
            {
                'access': access_token,
            }
        )

        # Set refresh token in secure HttpOnly cookie
        res.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            secure=True,  # Only over HTTPS
            samesite='Lax',  # Use 'Strict' or 'None' based on frontend setup
            max_age=7 * 24 * 60 * 60,  # 7 days
        )

        return res


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Get the refresh token from the cookie
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response(
                {'detail': 'Refresh token not found in cookie'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Inject the refresh token into the data
        serializer = self.get_serializer(data={'refresh': refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(
                {'detail': 'Invalid or expired refresh token'},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
