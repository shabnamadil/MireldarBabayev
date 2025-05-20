import factory
from tests.utils.helpers import generate_factory_content


class BaseSeoDetailFactory(factory.django.DjangoModelFactory):
    meta_description = factory.LazyFunction(lambda: generate_factory_content(50, 160))
    meta_keywords = factory.LazyFunction(lambda: generate_factory_content(50, 160))
    og_description = factory.LazyFunction(lambda: generate_factory_content(50, 160))

    class Meta:
        abstract = True
