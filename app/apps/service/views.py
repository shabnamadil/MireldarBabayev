from typing import Any
from django.utils import timezone
from django.views.generic import (
    ListView,
    DetailView
)

from .models import (
    Service,
    Download,
    WhyChooseUs,
    Coworker
)

from ..blog.models import Blog
from ..core.models import Testimoinal
from ..appointment.models import Timetable

class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'components/service/services.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        
        local_time = timezone.localtime(timezone.now())

        cx.update({
            'testimonials' : Testimoinal.objects.all()[:3],
            'why_choose_us' : WhyChooseUs.objects.all(),
            'coworkers' : Coworker.objects.all(),
            'available_times' : Timetable.objects.filter(
                start_time__gte=local_time,
                appointment=None
                )
        })
        return cx


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'components/service/partials/service-detail.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        obj = self.get_object()
        cx.update({
            'services' : Service.objects.all().exclude(id=obj.id),
            'downloads' : Download.objects.all(),
            'latest_blogs' : Blog.published.all()[:3],
            'why_choose_us' : WhyChooseUs.objects.all()
        })
        return cx
