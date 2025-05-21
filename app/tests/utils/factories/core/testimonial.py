import random

import factory
from apps.core.models import Testimoinal
from faker import Faker
from tests.utils.helpers import generate_factory_content

fake = Faker()


class TestimonialFactory(factory.django.DjangoModelFactory):
    client_image = factory.django.ImageField(color="blue", width=100, height=100)
    client_full_name = factory.LazyFunction(lambda: fake.name()[:20])
    client_profession = factory.LazyFunction(lambda: fake.job()[:100])
    client_comment = factory.LazyFunction(lambda: generate_factory_content(150, 155))
    star = factory.LazyFunction(lambda: random.randint(1, 5))

    class Meta:
        model = Testimoinal
