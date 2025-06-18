import factory
from apps.blog.models import Tag
from tests.utils.helpers import generate_factory_content


class TagFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(lambda: generate_factory_content(1, 80))

    class Meta:
        model = Tag
