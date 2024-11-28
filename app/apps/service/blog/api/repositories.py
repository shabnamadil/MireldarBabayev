from django.db.models import Q

from ..models import (
    Blog,
    Comment
)


class BlogRepository:
    DEFAULT_QS = Blog.published.all()
    
    def __init__(self):
        self.model = Blog

    def get_by_category(self, category_slug, qs=DEFAULT_QS):
        return qs.filter(category__slug=category_slug)
    
    def get_by_tag(self, tag_slug, qs=DEFAULT_QS):
        return qs.filter(tag__slug=tag_slug)
    
    def get_by_query(self, query, qs=DEFAULT_QS):
        return qs.filter(
            Q(title__contains=query) | 
            Q(short_description__contains=query) |
            Q(content__contains=query) |
            Q(category__name__contains=query) |
            Q(tag__name__contains=query) |
            Q(author__first_name__contains=query) |
            Q(author__last_name__contains=query)                    
            )
    
    def get_by_page(self, page=1, qs=DEFAULT_QS):
        items_per_page = 3
        start = (int(page) - 1) * items_per_page
        end = start + items_per_page
        return qs[start:end]


class CommentRepository:
    DEFAULT_QS = Comment.objects.all()
    
    def __init__(self):
        self.model = Comment

    def get_by_blog(self, blog_id, qs=DEFAULT_QS):
        return qs.filter(blog__id=blog_id)