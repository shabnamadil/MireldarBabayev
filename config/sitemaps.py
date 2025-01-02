from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.blog.models import Blog
from apps.service.models import Service


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    i18n = True
    limit = 1000

    def __init__(self, language):
        self.language = language

    def items(self):
        return [
            'home', 'about', 'contact',
            'faq', 'services', 'blogs',
        ]

    def location(self, item):
        return reverse(item)
    

class BlogSitemap(Sitemap):
    changefreq = "daily" 
    priority = 0.9
    protocol = 'https'
    i18n = True
    limit = 1000

    def __init__(self, language):
        self.language = language

    def items(self):
        return Blog.published.all()

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return f"/{self.language}/blogs/{obj.slug}/"
    

class ServiceSitemap(Sitemap):
    changefreq = "weekly" 
    priority = 0.8 
    i18n = True
    limit = 1000

    def __init__(self, language):
        self.language = language

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return f"/{self.language}/services/{obj.slug}/"
