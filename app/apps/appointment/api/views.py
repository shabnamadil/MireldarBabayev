from rest_framework.generics import CreateAPIView

from .serializers import AppointmentPostSerializer


class AppointmentPostAPIView(CreateAPIView):
    serializer_class = AppointmentPostSerializer
