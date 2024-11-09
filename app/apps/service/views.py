from typing import Any
from django.shortcuts import render
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

from apps.blog.models import Blog
from apps.core.models import Testimoinal

class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'components/service/services.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        cx = super().get_context_data(**kwargs)
        cx.update({
            'testimonials' : Testimoinal.objects.all()[:3],
            'why_choose_us' : WhyChooseUs.objects.all(),
            'coworkers' : Coworker.objects.all()
        })
        return cx


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'components/service/partials/service-detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        cx = super().get_context_data(**kwargs)
        obj = self.get_object()
        cx.update({
            'services' : Service.objects.all().exclude(id=obj.id),
            'downloads' : Download.objects.all(),
            'latest_blogs' : Blog.published.all()[:3],
            'why_choose_us' : WhyChooseUs.objects.all()
        })
        return cx