from apps.service.models import Coworker
from tests.utils.factories import CoworkerFactory
from tests.utils.helpers import _PngValidationTest
from utils.tests.base import BaseValidationTest


class TestCoworkerModelIntegration(BaseValidationTest, _PngValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = CoworkerFactory
        cls.object = CoworkerFactory()
        cls.model = Coworker

    def test_name_max_length(self):
        self.assert_max_length(self.object, "name", 100)

    def test_name_unique(self):
        self.assert_unique_field(self.model, "name", self.object.name)

    def test_name_required(self):
        self.assert_required_field(self.object, "name")

    def test_png_required(self):
        self.assert_required_field(self.object, "png")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_coworker_name_saved_correctly(self):
        self.assert_model_instance(self.object, "name", self.object.name)

    def test_coworker_png_saved_correctly(self):
        self.assertTrue(self.object.png.name.startswith("coworkers/"))
        self.assertTrue(self.object.png.name.endswith(".png"))

    def test_object_is_instance_of_coworker(self):
        self.assertIsInstance(self.object, self.model)

    def test_coworkers_are_ordered_by_created_at_desc(self):
        self.assert_ordering(CoworkerFactory, self.model)
