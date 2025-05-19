import random

import factory
from apps.service.models import Download
from tests.utils.helpers import (
    generate_dummy_file,
)

from .service import ServiceFactory


class DownloadFactory(factory.django.DjangoModelFactory):
    type = factory.LazyFunction(lambda: random.choice(['pdf', 'docx']))
    file = factory.LazyAttribute(lambda o: generate_dummy_file(o.type))
    service = factory.SubFactory(ServiceFactory)

    class Meta:
        model = Download
