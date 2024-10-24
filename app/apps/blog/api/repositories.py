from ..models import Blog


class BlogRepository:
    DEFAULT_QS = Blog.published.all()
    
    def __init__(self):
        self.model = Blog

    def get_by_category(self, category_name, qs=DEFAULT_QS):
        return qs.filter(category__name=category_name)
    
    def get_by_tag(self, tag_name, qs=DEFAULT_QS):
        return qs.filter(tag__name=tag_name)