from django.utils import timezone
from django.views.generic import TemplateView

from apps.core.models import Testimoinal, WhoWeAre
from apps.seo.models import AppointmentPageSeo
from apps.service.models import WhyChooseUs

from .models import Timetable


class AppointmentPageView(TemplateView):
    template_name = "components/appointment/appointment.html"

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        local_time = timezone.localtime(timezone.now())
        cx.update(
            {
                "who_we_are": WhoWeAre.objects.first(),
                "testimonials": Testimoinal.objects.all()[:4],
                "why_choose_us": WhyChooseUs.objects.all(),
                "seo": AppointmentPageSeo.objects.first(),
                "available_times": Timetable.objects.filter(
                    start_time__gte=local_time, appointment=None
                ),
            }
        )
        return cx
