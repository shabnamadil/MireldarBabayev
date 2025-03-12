from django import forms
from django.utils import timezone

from .models import Appointment, Timetable


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ("id", "start_time", "end_time")

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")  # Will be None if missing
        end = cleaned_data.get("end_time")

        local_time = timezone.localtime(timezone.now())

        if start is None:
            pass
        elif start < local_time:
            self.add_error(
                "start_time",
                "The start time must be in the future.",
            )

        if end is None:
            pass
        elif (
            start and end < start
        ):  # Ensure 'start' is not None before comparison
            self.add_error(
                "end_time",
                "The end time must be after the start time.",
            )

        if start == end:
            self.add_error(
                "",
                "Start and End time cannot be same",
            )

        return cleaned_data  # Always return cleaned_data


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = (
            "id",
            "full_name",
            "phone",
            "location",
            "message",
            "available_time",
        )

    def clean_available_time(self):
        time = self.cleaned_data.get("available_time")

        if not time:  # Ensure time is provided
            raise forms.ValidationError("Available time is required.")

        start = time.start_time
        end = time.end_time
        local_time = timezone.localtime(timezone.now())

        if start and start < local_time:
            raise forms.ValidationError(
                "The start time must be in the future."
            )

        if end and start and end < start:
            raise forms.ValidationError(
                "The end time must be after the start time."
            )

        if start == end:
            raise forms.ValidationError(
                "Start and End time cannot be the same."
            )

        return time  # ✅ Return the cleaned field, not cleaned_data
