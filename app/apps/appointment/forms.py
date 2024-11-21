from typing import Any
from django import forms
from django.utils import timezone

from .models import (
    Timetable,
    Appointment
)


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = (
            'id',
            'start_time',
            'end_time'
        )

    def clean(self) -> dict[str, Any]:
        start = self.cleaned_data.get('start_time', '')
        end = self.cleaned_data.get('end_time', '')

        # Convert to local time for comparison
        local_time = timezone.localtime(timezone.now())

        # Validate that 'start_time' is in the future
        if start and start < local_time:
            raise forms.ValidationError('The start time must be in the future.')

        # Validate that 'end_time' is after 'start_time'
        if end and end < start:
            raise forms.ValidationError('The end time must be after the start time.')

        return super().clean()
    

class AppointmentForm(forms.ModelForm):
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

    def clean_phone(self) -> str:
        phone = self.cleaned_data.get('phone', '')
        if phone.startswith('+'):
            phone_without_plus = phone[1:]
        else:
            phone_without_plus = phone

        if phone_without_plus and not phone_without_plus.isdigit():
            raise forms.ValidationError('Only numeric values are allowed.')

        if phone_without_plus and len(phone_without_plus) < 10:
            raise forms.ValidationError('Phone number must be at least 10 characters.')
        
        return phone_without_plus
    
    def clean_available_time(self):
        time = self.cleaned_data.get('available_time', '')
        start = time.start_time
        end = time.end_time

        # Convert to local time for comparison
        local_time = timezone.localtime(timezone.now()).time()

        # Validate that 'start_time' is in the future
        if start and start < local_time:
            raise forms.ValidationError('The start time must be in the future.')

        # Validate that 'end_time' is after 'start_time'
        if end and end < start:
            raise forms.ValidationError('The end time must be after the start time.')