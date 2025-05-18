import factory
from apps.service.models import Service
from tests.utils.helpers import generate_factory_content, generate_png_file


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = factory.LazyFunction(lambda: generate_factory_content(1, 30))
    short_description = factory.LazyFunction(lambda: generate_factory_content(145, 160))
    title = factory.LazyFunction(lambda: generate_factory_content(30, 60))
    content = factory.LazyFunction(lambda: generate_factory_content(300, 1000))
    background_color = "blue"
    png = factory.LazyFunction(generate_png_file)
    image = factory.django.ImageField(color="blue", width=100, height=100)
