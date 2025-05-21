import factory
from apps.core.models import SiteSettings
from faker import Faker
from tests.utils.helpers import (
    generate_factory_content,
    generate_png_file,
)

fake = Faker()


class SiteSettingsFactory(factory.django.DjangoModelFactory):
    site_name = factory.LazyFunction(lambda: generate_factory_content(30, 100))
    logo = factory.LazyFunction(generate_png_file)
    favicon = factory.LazyFunction(generate_png_file)
    location = factory.Faker("word")
    number = factory.LazyFunction(lambda: "+12025550173")
    email = factory.Faker("email")
    work_hours = factory.LazyFunction(lambda: "09:00 - 18:00")
    map_url = factory.LazyFunction(
        lambda: 'https://www.google.com/maps/embed?pb=!1m14!1m8!1mz'
    )

    facebook = factory.LazyFunction(lambda: "https://www.facebook.com/examplepage")
    youtube = factory.LazyFunction(lambda: "https://www.youtube.com/channel/example")
    twitter = factory.LazyFunction(lambda: "https://www.twitter.com/example")
    instagram = factory.LazyFunction(lambda: "https://www.instagram.com/example")
    linkedin = factory.LazyFunction(lambda: "https://www.linkedin.com/in/example")
    tiktok = factory.LazyFunction(lambda: "https://www.tiktok.com/@example")

    footer_description = factory.LazyFunction(lambda: generate_factory_content(1, 200))

    class Meta:
        model = SiteSettings
