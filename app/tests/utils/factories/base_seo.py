import factory
from tests.utils.helpers import generate_factory_content


class BaseSeoFactory(factory.django.DjangoModelFactory):
    meta_title = factory.LazyFunction(lambda: generate_factory_content(30, 60))
    meta_description = factory.LazyFunction(lambda: generate_factory_content(50, 160))
    meta_keywords = factory.LazyFunction(lambda: generate_factory_content(50, 160))
    meta_keywords = factory.LazyFunction(lambda: generate_factory_content(50, 160))
    og_title = factory.LazyFunction(lambda: generate_factory_content(30, 60))
    og_description = factory.LazyFunction(lambda: generate_factory_content(50, 160))
    og_image = factory.django.ImageField(color="blue", width=100, height=100)

    class Meta:
        abstract = True
