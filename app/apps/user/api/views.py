from rest_framework.generics import (
    CreateAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    RegisterSerializer
)

class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer