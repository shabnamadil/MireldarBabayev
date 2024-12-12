from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone

from .models import Timetable
from apps.core.models import (
    WhoWeAre,
    Testimoinal
)
from apps.service.models import WhyChooseUs


class AppointmentPageView(TemplateView):
    template_name = 'components/appointment/appointment.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        local_time = timezone.localtime(timezone.now())
        cx.update({
            'who_we_are' : WhoWeAre.objects.first(),
            'testimonials' : Testimoinal.objects.all()[:4],
            'why_choose_us' : WhyChooseUs.objects.all(),
            'available_times' : Timetable.objects.filter(
                start_time__gte=local_time,
                appointment=None
                )
        })
        return cx
