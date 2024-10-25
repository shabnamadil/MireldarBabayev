from rest_framework.generics import (
    CreateAPIView
)

from .serializers import (
    NewsletterPostSerializer,
    ContactPostSerializer
)


class NewsletterCreateAPIView(CreateAPIView):
    serializer_class = NewsletterPostSerializer


class ContactPostAPIView(CreateAPIView):
    serializer_class = ContactPostSerializer