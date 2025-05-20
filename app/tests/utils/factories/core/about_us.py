import factory
from apps.core.models import AboutUs


class AboutUsFactory(factory.django.DjangoModelFactory):
    image = factory.django.ImageField(color="blue", width=100, height=100)
    video_id = factory.LazyFunction(lambda: "MKG_6BqnhpI")
    content = factory.Faker("sentence", nb_words=10)
    mission = factory.Faker("sentence", nb_words=10)
    vision = factory.Faker("sentence", nb_words=10)
    value = factory.Faker("sentence", nb_words=10)

    class Meta:
        model = AboutUs
