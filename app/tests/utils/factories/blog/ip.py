import factory
from apps.blog.models import IP  # Update this import to match your actual app path
from faker import Faker

fake = Faker()


class IPFactory(factory.django.DjangoModelFactory):
    view_ip = factory.LazyFunction(fake.ipv4)

    class Meta:
        model = IP
