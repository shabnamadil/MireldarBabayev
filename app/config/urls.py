"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from typing import Dict

from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from utils.errors.custom_errors import custom_404, custom_500

from .sitemaps import BlogSitemap, ServiceSitemap, StaticSitemap

handler404 = custom_404
handler500 = custom_500

languages = ['en', 'az', 'ru']
sitemaps: Dict[str, Sitemap] = {}

for lang in languages:
    sitemaps[f'blog-{lang}'] = BlogSitemap(language=lang)
    sitemaps[f'service-{lang}'] = ServiceSitemap(language=lang)
    sitemaps[f'static-{lang}'] = StaticSitemap(language=lang)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('apps.blog.api.urls')),
    path('api/', include('apps.core.api.urls')),
    path('api/', include('apps.appointment.api.urls')),
    path('api/', include('apps.user.api.urls')),
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain"
        ),
    ),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps, 'template_name': 'custom_sitemap.xml'},
        name='django.contrib.sitemaps.views.sitemap',
    ),
    path("django-check-seo/", include("django_check_seo.urls")),
]

urlpatterns += i18n_patterns(
    path('set_language/', include('django.conf.urls.i18n')),
    path('', include('apps.blog.urls')),
    path('', include('apps.core.urls')),
    path('', include('apps.service.urls')),
    path('', include('apps.appointment.urls')),
    path('', include('apps.user.urls')),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [re_path(r'^rosetta/', include('rosetta.urls'))]
