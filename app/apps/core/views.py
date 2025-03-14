from django.utils import timezone
from django.views.generic import DetailView, ListView, TemplateView

from ..appointment.models import Timetable
from ..blog.models import Blog
from ..seo.models import (
    AboutUsPageSeo,
    ContactPageSeo,
    FaqPageSeo,
    HomePageSeo,
)
from ..service.models import Service, WhyChooseUs
from .models import (
    AboutUs,
    Banner,
    Faq,
    StatisticalIndicator,
    Testimoinal,
    WhoWeAre,
)


class ContactPageView(TemplateView):
    template_name = 'components/contact/contact.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)

        cx.update({'seo': ContactPageSeo.objects.first()})

        return cx


class AboutUsPageView(DetailView):
    template_name = 'components/about/about-us.html'
    model = AboutUs
    context_object_name = 'about'

    def get_object(self, queryset=None):
        return AboutUs.objects.first()

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)

        statistics = StatisticalIndicator.objects.all()[:4]
        colors = ['yellow', 'blue', 'green', 'gray']

        # Pair each statistic with a color
        paired_statistics = zip(statistics, colors)

        cx.update(
            {
                'paired_statistics': paired_statistics,
                'who_we_are': WhoWeAre.objects.first(),
                'testimonials': Testimoinal.objects.all(),
                'seo': AboutUsPageSeo.objects.first(),
            }
        )
        return cx


class HomePageView(TemplateView):
    template_name = 'components/home/index.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)

        statistics = StatisticalIndicator.objects.all()[:4]
        colors = ['yellow', 'blue', 'green', 'gray']
        paired_statistics = zip(statistics, colors)

        local_time = timezone.localtime(timezone.now())

        cx.update(
            {
                'banners': Banner.objects.all(),
                'about': AboutUs.objects.first(),
                'paired_statistics': paired_statistics,
                'services': Service.objects.all()[:4],
                'why_choose_us': WhyChooseUs.objects.all()[:4],
                'testimonials': Testimoinal.objects.all()[:4],
                'blogs': Blog.published.all()[:4],
                'seo': HomePageSeo.objects.first(),
                'available_times': Timetable.objects.filter(
                    start_time__gte=local_time, appointment=None
                ),
            }
        )
        return cx


class FaqListView(ListView):
    model = Faq
    template_name = 'components/core/faq.html'
    context_object_name = 'faqs'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)

        cx.update({'seo': FaqPageSeo.objects.first()})

        return cx
