import factory
from apps.service.models import Service
from tests.utils.helpers import generate_png_file


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = "Test name"
    short_description = "Test short description"
    png = factory.LazyFunction(generate_png_file)
    image = factory.django.ImageField(color='blue', width=100, height=100)
    title = "Test title"
    content = "Test content"
    background_color = "blue"
