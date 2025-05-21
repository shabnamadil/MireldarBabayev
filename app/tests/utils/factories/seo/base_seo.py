import factory
from tests.utils.helpers import generate_factory_content

from .base_seo_detail import BaseSeoDetailFactory


class BaseSeoFactory(BaseSeoDetailFactory):
    meta_title = factory.LazyFunction(lambda: generate_factory_content(30, 60))
    og_title = factory.LazyFunction(lambda: generate_factory_content(30, 60))
    og_image = factory.django.ImageField(color="blue", width=100, height=100)

    class Meta:
        abstract = True
