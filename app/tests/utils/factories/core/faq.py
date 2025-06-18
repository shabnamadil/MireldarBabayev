import factory
from apps.core.models import Faq


class FaqFactory(factory.django.DjangoModelFactory):
    question = factory.Faker("sentence", nb_words=10)
    response = factory.Faker("sentence", nb_words=10)

    class Meta:
        model = Faq
