import factory
from apps.blog.models import Comment

from ..blog.blog import BlogFactory
from ..user.user import UserFactory


class CommentFactory(factory.django.DjangoModelFactory):
    content = factory.Faker("sentence", nb_words=10)
    blog = factory.SubFactory(BlogFactory)
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Comment
