from apps.service.models import WhyChooseUs
from tests.utils.helpers import BaseValidationTest


class TestWhyChooseUsModel(BaseValidationTest):

    def test_why_choose_us_object_str_returns_title(self):
        self.assert_str_output(WhyChooseUs, "title", "Test title")
