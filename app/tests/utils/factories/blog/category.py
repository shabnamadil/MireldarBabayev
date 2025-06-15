import factory
from apps.blog.models import Category
from tests.utils.helpers import generate_factory_content


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(lambda: generate_factory_content(1, 150))

    class Meta:
        model = Category
