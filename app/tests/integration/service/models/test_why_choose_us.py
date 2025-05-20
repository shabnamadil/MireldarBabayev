from apps.service.models import WhyChooseUs
from tests.utils.factories import WhyChooseUsFactory
from tests.utils.helpers import _PngValidationTest
from utils.tests.base import BaseValidationTest


class TestWhyChooseUsModelIntegration(BaseValidationTest, _PngValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = WhyChooseUsFactory
        cls.object = cls.factory()
        cls.model = WhyChooseUs

    def test_title_max_length(self):
        self.assert_max_length(self.object, "title", 30)

    def test_short_description_max_length(self):
        self.assert_max_length(self.object, "short_description", 60)

    def test_short_description_min_length(self):
        self.assert_min_length(self.object, "short_description", 50)

    def test_title_unique(self):
        self.assert_unique_field(self.model, "title", self.object.title)

    def test_short_description_unique(self):
        self.assert_unique_field(
            self.model, "short_description", self.object.short_description
        )

    def test_title_required(self):
        self.assert_required_field(self.object, "title")

    def test_short_description_required(self):
        self.assert_required_field(self.object, "short_description")

    def test_png_required(self):
        self.assert_required_field(self.object, "png")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_why_choose_us_title_saved_correctly(self):
        self.assert_model_instance(self.object, "title", self.object.title)

    def test_why_choose_us_short_description_saved_correctly(self):
        self.assert_model_instance(
            self.object, "short_description", self.object.short_description
        )

    def test_why_choose_us_png_saved_correctly(self):
        self.assertTrue(self.object.png.name.startswith("why_choose_us/"))
        self.assertTrue(self.object.png.name.endswith(".png"))

    def test_object_is_instance_of_why_choose_us(self):
        self.assertIsInstance(self.object, self.model)

    def test_why_choose_us_objects_are_ordered_by_created_at_desc(self):
        self.assert_ordering(self.factory, self.model)
