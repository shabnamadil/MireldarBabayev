from rest_framework import serializers

from ..models import (
    Appointment
)


class AppointmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'id',
            'full_name',
            'phone',
            'location',
            'message',
            'available_time'
        )