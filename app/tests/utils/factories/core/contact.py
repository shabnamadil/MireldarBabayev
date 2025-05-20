import factory
from apps.core.models import Contact
from tests.utils.helpers import (
    generate_factory_content,
)


class ContactFactory(factory.django.DjangoModelFactory):
    first_name = factory.LazyFunction(lambda: generate_factory_content(1, 20))
    last_name = factory.LazyFunction(lambda: generate_factory_content(1, 20))
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")
    message = factory.Faker("sentence", nb_words=10)

    class Meta:
        model = Contact
