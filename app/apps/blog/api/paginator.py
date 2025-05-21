from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BlogPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "results": data,
                "has_next": self.page.has_next(),
                "has_previous": self.page.has_previous(),
                "current_page": self.page.number,
                "total_pages": self.page.paginator.num_pages,
            }
        )
