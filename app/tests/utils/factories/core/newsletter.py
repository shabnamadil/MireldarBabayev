import factory
from apps.core.models import Newsletter


class NewsletterFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = Newsletter
