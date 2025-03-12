from rest_framework.generics import CreateAPIView

from .serializers import (
    ContactPostSerializer,
    NewsletterPostSerializer,
)


class NewsletterCreateAPIView(CreateAPIView):
    serializer_class = NewsletterPostSerializer


class ContactPostAPIView(CreateAPIView):
    serializer_class = ContactPostSerializer
