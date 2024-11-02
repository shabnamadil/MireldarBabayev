from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    BlogListSerializer,
    CommentPostSerializer,
    CommentUpdateDestroySerializer
)
from .repositories import BlogRepository
from ..models import (
    Blog,
    Comment
)
from .permissions import IsCommentAuthor


class BlogListAPIView(ListAPIView):
    queryset = Blog.published.select_related('author').prefetch_related(
        'category', 'tag', 'comments__author'
    )
    serializer_class = BlogListSerializer
    repo = BlogRepository

    def get_filter_methods(self):
        repo = self.repo()
        return {
            'category' : repo.get_by_category,
            'tag' : repo.get_by_tag,
            'q' : repo.get_by_query,
            'p' : repo.get_by_page
        }

    def get_queryset(self, **kwargs):
        qs = Blog.published.all()
        filters = self.get_filter_methods()
        
        for key, value in self.request.query_params.items():
            if key in filters:
                qs = filters[key](value, qs)
        return qs
    

class CommentPostAPIView(CreateAPIView):
    serializer_class = CommentPostSerializer
    permission_classes = (IsAuthenticated, )


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentUpdateDestroySerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated, IsCommentAuthor)