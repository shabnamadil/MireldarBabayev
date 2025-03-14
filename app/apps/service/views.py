from django.utils import timezone
from django.views.generic import DetailView, ListView

from apps.seo.models import ServiceDetailPageSeo, ServicesPageSeo

from ..appointment.models import Timetable
from ..blog.models import Blog
from ..core.models import Testimoinal
from .models import Coworker, Service, WhyChooseUs


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'components/service/services.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)

        local_time = timezone.localtime(timezone.now())

        cx.update(
            {
                'testimonials': Testimoinal.objects.all()[:3],
                'why_choose_us': WhyChooseUs.objects.all(),
                'coworkers': Coworker.objects.all(),
                'seo': ServicesPageSeo.objects.first(),
                'available_times': Timetable.objects.filter(
                    start_time__gte=local_time, appointment=None
                ),
            }
        )
        return cx


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'components/service/partials/service-detail.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        obj = self.get_object()
        cx.update(
            {
                'services': Service.objects.all().exclude(id=obj.id),
                'latest_blogs': Blog.published.all()[:3],
                'why_choose_us': WhyChooseUs.objects.all(),
                'seo': ServiceDetailPageSeo.objects.get(service__id=obj.id),
            }
        )
        return cx
