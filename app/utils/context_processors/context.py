import datetime

from apps.core.models import (
    SiteSettings,
    StatisticalIndicator
)

def context_info(request):
    context={
        'current_year': datetime.datetime.now().year,
        'current_time': datetime.datetime.now(),
        'settings': SiteSettings.objects.first(),
        'indicators' : StatisticalIndicator.objects.all()[:3]
    }
    return context