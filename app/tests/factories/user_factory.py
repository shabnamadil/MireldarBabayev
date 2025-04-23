from django.contrib.auth import get_user_model

import factory

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = "test@gmail.com"
    password = factory.PostGenerationMethodCall('set_password', 'testpassword')
    first_name = "John"
    last_name = "Doe"
    image = factory.django.ImageField(color='blue', width=100, height=100)
