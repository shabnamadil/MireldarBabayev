import factory
from apps.core.models import StatisticalIndicator
from tests.utils.helpers import (
    generate_factory_content,
    generate_png_file,
)


class StatisticalIndicatorFactory(factory.django.DjangoModelFactory):
    png = factory.LazyFunction(generate_png_file)
    value = factory.Faker("random_int", min=0, max=10000)
    name = factory.LazyFunction(lambda: generate_factory_content(1, 50))

    class Meta:
        model = StatisticalIndicator
