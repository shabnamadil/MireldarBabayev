import factory
from apps.core.models import WhoWeAre
from faker import Faker
from tests.utils.helpers import generate_factory_content, generate_video_id

fake = Faker()


class WhoWeAreFactory(factory.django.DjangoModelFactory):
    title = factory.LazyFunction(lambda: generate_factory_content(1, 50))
    video_link = factory.LazyFunction(generate_video_id)
    content = factory.Faker("sentence", nb_words=10)

    class Meta:
        model = WhoWeAre
