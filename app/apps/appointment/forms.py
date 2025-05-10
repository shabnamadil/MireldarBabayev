from django import forms

from utils.validators.validate_time import (
    validate_future_time,
    validate_start_end_times,
)

from .models import Appointment, Timetable


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ('id', 'start_time', 'end_time')

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_time')
        end = cleaned_data.get('end_time')

        validate_future_time(start, 'start_time')
        validate_start_end_times(start, end)

        return cleaned_data


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = (
            'id',
            'full_name',
            'phone',
            'location',
            'message',
            'available_time',
        )

    def clean_available_time(self):
        time = self.cleaned_data.get('available_time')

        if not time:
            raise forms.ValidationError("Available time is required.")

        validate_future_time(time.start_time, 'available_time')
        validate_start_end_times(time.start_time, time.end_time)

        return time
