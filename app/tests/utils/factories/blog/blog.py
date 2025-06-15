import factory
from apps.blog.models import Blog
from tests.utils.helpers import generate_factory_content

from ..user.user import UserFactory
from .category import CategoryFactory
from .tag import TagFactory


class BlogFactory(factory.django.DjangoModelFactory):
    title = factory.LazyFunction(lambda: generate_factory_content(1, 100))
    short_description = factory.LazyFunction(lambda: generate_factory_content(1, 200))
    content = factory.Faker("sentence", nb_words=10)
    image = factory.django.ImageField(color="blue", width=100, height=100)
    author = factory.SubFactory(UserFactory)
    status = Blog.Status.PUBLISHED

    class Meta:
        model = Blog

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for cat in extracted:
                self.category.add(cat)
        else:
            self.category.add(CategoryFactory())

    @factory.post_generation
    def tag(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for t in extracted:
                self.tag.add(t)
        else:
            self.tag.add(TagFactory())
