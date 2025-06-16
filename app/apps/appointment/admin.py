from django.contrib import admin

from .forms import AppointmentForm, TimetableForm
from .models import Appointment, Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time")
    list_filter = ("created_at",)
    list_per_page = 20
    date_hierarchy = "created_at"
    form = TimetableForm


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "available_time")
    list_filter = ("created_at",)
    list_per_page = 20
    date_hierarchy = "created_at"
    form = AppointmentForm
