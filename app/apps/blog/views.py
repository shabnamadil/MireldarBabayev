from typing import Any
from django.shortcuts import render
from django.db.models import Count

from django.views.generic import (
    TemplateView,
    DetailView
)

from .models import (
    Blog,
    IP,
    Category,
    Tag
)
from utils.helpers.client_ip import get_client_ip


class BlogListView(TemplateView):
    template_name = 'components/blog/blog-list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        cx =  super().get_context_data(**kwargs)
        cx['popular_blogs'] = Blog.published.annotate(
            comment_count=Count('comments')
            ).order_by('-comment_count', '-view_count')[:3]
        cx['categories'] = Category.objects.all()
        cx['tags'] = Tag.objects.all()
        return cx


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'components/blog/blog-detail.html'

    def get(self, request, *args , **kwargs):
        obj = self.get_object()
        ip = get_client_ip(request)
        ip_obj, created = IP.objects.get_or_create(view_ip=ip)
        obj.increment_view_count(ip_obj)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        obj = self.get_object()
        cx =  super().get_context_data(**kwargs)
        cx['popular_blogs'] = Blog.published.annotate(
            comment_count=Count('comments')
            ).exclude(id=obj.id).order_by(
                '-comment_count', '-view_count')[:3]
        cx['categories'] = Category.objects.all()
        cx['tags'] = Tag.objects.all()
        return cx