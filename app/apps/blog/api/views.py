from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
)

from .serializers import (
    BlogListSerializer,
    CommentPostSerializer,
    CommentUpdateDestroySerializer,
    CommentListSerializer
)
from .repositories import (
    BlogRepository,
    CommentRepository
)
from ..models import (
    Blog,
    Comment
)
from .permissions import IsCommentAuthor
from .paginator import BlogPagination



class BlogListAPIView(ListAPIView):
    queryset = Blog.published.select_related('author').prefetch_related(
        'category', 'tag', 'comments__author'
    )
    serializer_class = BlogListSerializer
    repo = BlogRepository
    pagination_class = BlogPagination

    def get_filter_methods(self):
        repo = self.repo()
        return {
            'category' : repo.get_by_category,
            'tag' : repo.get_by_tag,
            'q' : repo.get_by_query
        }

    def get_queryset(self, **kwargs):
        qs = Blog.published.all()
        filters = self.get_filter_methods()
        
        for key, value in self.request.query_params.items():
            if key in filters:
                qs = filters[key](value, qs)
        return qs
    

class CommentListPostAPIView(ListCreateAPIView):
    serializer_class = CommentListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Comment.objects.all()
    repo = CommentRepository

    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = CommentPostSerializer
        return super().get_serializer_class()
    
    def get_filter_methods(self):
        repo = self.repo()
        return {
            'blog' : repo.get_by_blog
        }

    def get_queryset(self, **kwargs):
        qs = Comment.objects.all()
        filters = self.get_filter_methods()
        
        for key, value in self.request.query_params.items():
            if key in filters:
                qs = filters[key](value, qs)
        return qs
    


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentUpdateDestroySerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated, IsCommentAuthor)