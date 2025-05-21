import factory
from apps.core.models import Contact
from tests.utils.helpers import (
    generate_factory_content,
)


class ContactFactory(factory.django.DjangoModelFactory):
    first_name = factory.LazyFunction(lambda: generate_factory_content(1, 20))
    last_name = factory.LazyFunction(lambda: generate_factory_content(1, 20))
    email = factory.Faker("email")
    phone = factory.LazyFunction(lambda: "+12025550173")
    message = factory.Faker("sentence", nb_words=10)

    class Meta:
        model = Contact
