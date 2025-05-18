import factory
from apps.service.models import WhyChooseUs
from tests.utils.helpers import generate_factory_content, generate_png_file


class WhyChooseUsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WhyChooseUs

    title = factory.LazyFunction(lambda: generate_factory_content(1, 30))
    short_description = factory.LazyFunction(lambda: generate_factory_content(50, 60))
    png = factory.LazyFunction(generate_png_file)
