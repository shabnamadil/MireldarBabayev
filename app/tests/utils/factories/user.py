from django.contrib.auth import get_user_model

import factory

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'testpassword')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    image = factory.django.ImageField(color='blue', width=100, height=100)

    class Meta:
        model = User
