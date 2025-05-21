from apps.core.models import StatisticalIndicator
from tests.utils.factories import StatisticalIndicatorFactory
from tests.utils.helpers import (
    BaseValidationTest,
    _PngValidationTest,
)


class TestStatisticalIndicatorModelIntegration(BaseValidationTest, _PngValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = StatisticalIndicatorFactory
        cls.object = cls.factory()
        cls.model = StatisticalIndicator
        cls.png_field = "png"

    def test_name_max_length(self):
        self.assert_max_length(self.object, "name", 50)

    def test_name_unique(self):
        self.assert_unique_field(self.model, "name", self.object.name)

    def test_name_required(self):
        self.assert_required_field(self.object, "name")

    def test_value_required(self):
        self.assert_required_field(self.object, "value")

    def test_png_required(self):
        self.assert_required_field(self.object, "png")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_name_saved_correctly(self):
        self.assert_model_instance(self.object, "name", self.object.name)

    def test_value_saved_correctly(self):
        self.assert_model_instance(self.object, "value", self.object.value)

    def test_png_saved_correctly(self):
        self.assertTrue(self.object.png.name.startswith("statistics/"))
        self.assertTrue(self.object.png.name.endswith(".png"))

    def test_object_is_instance_of_indicator(self):
        self.assertIsInstance(self.object, self.model)

    def test_indicators_are_ordered_by_created_at_desc(self):
        self.assert_ordering(self.factory, self.model)
