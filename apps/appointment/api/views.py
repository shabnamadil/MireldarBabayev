from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)

from .serializers import (
    AppointmentPostSerializer
)

from ..models import Timetable


class AppointmentPostAPIView(CreateAPIView):
    serializer_class = AppointmentPostSerializer