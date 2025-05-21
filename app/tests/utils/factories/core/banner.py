import factory
from apps.core.models import Banner
from tests.utils.helpers import (
    generate_factory_content,
    generate_png_file,
    generate_video_id,
)


class BannerFactory(factory.django.DjangoModelFactory):
    title = factory.LazyFunction(lambda: generate_factory_content(1, 100))
    subtitle = factory.LazyFunction(lambda: generate_factory_content(1, 100))
    description = factory.Faker("sentence", nb_words=10)
    png = factory.LazyFunction(generate_png_file)
    video_id = factory.LazyFunction(generate_video_id)

    class Meta:
        model = Banner
