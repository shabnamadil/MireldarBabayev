import factory
from apps.service.models import Coworker
from tests.utils.helpers import generate_factory_content, generate_png_file


class CoworkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Coworker

    name = factory.LazyFunction(lambda: generate_factory_content(1, 100))
    png = factory.LazyFunction(generate_png_file)
