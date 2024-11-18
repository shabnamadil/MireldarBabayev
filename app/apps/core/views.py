from typing import Any
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView
)

from .models import (
    AboutUs,
    StatisticalIndicator,
    WhoWeAre,
    Testimoinal,
    Banner,
    Faq
)

from apps.service.models import (
    Service,
    WhyChooseUs
)

from apps.blog.models import Blog

class ContactPageView(TemplateView):
    template_name = 'components/contact/contact.html'


class AboutUsPageView(DetailView):
    template_name = 'components/about/about-us.html'
    model = AboutUs
    context_object_name = 'about'

    def get_object(self, queryset=None):
        return AboutUs.objects.first()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        cx =  super().get_context_data(**kwargs)

        statistics = StatisticalIndicator.objects.all()[:4]
        colors = ['yellow', 'blue', 'green', 'gray']
        
        # Pair each statistic with a color
        paired_statistics = zip(statistics, colors)

        cx.update({
            'paired_statistics': paired_statistics,
            'who_we_are' : WhoWeAre.objects.first(),
            'testimonials' : Testimoinal.objects.all()
        })
        return cx
    

class HomePageView(TemplateView):
    template_name = 'components/home/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        cx = super().get_context_data(**kwargs)

        statistics = StatisticalIndicator.objects.all()[:4]
        colors = ['yellow', 'blue', 'green', 'gray']
        
        # Pair each statistic with a color
        paired_statistics = zip(statistics, colors)
        cx.update({
            'banners': Banner.objects.all(),
            'about': AboutUs.objects.first(),
            'paired_statistics': paired_statistics,
            'services': Service.objects.all()[:4],
            'why_choose_us': WhyChooseUs.objects.all()[:4],
            'testimonials' : Testimoinal.objects.all()[:4],
            'blogs': Blog.published.all()[:4]
        })
        return cx
    

class FaqListView(ListView):
    model = Faq
    template_name = 'components/core/faq.html'
    context_object_name = 'faqs'