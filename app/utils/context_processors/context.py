import datetime

from django.contrib.sites.models import Site

from apps.core.models import SiteSettings, StatisticalIndicator
from apps.service.models import Service


def context_info(request):
    site = Site.objects.get_current()
    site_url = site.domain

    context = {
        "current_year": datetime.datetime.now().year,
        "current_time": datetime.datetime.now(),
        "settings": SiteSettings.objects.first(),
        "indicators": StatisticalIndicator.objects.all()[:3],
        "footer_services": Service.objects.all(),
        "site_url": site_url,
    }
    return context
