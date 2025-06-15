from apps.blog.models import Category
from tests.utils.factories import CategoryFactory
from tests.utils.helpers import (
    BaseValidationTest,
)


class TestCategoryModelIntegration(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = CategoryFactory
        cls.object = cls.factory()
        cls.model = Category

    def test_name_max_length(self):
        self.assert_max_length(self.object, "name", 150)

    def test_name_unique(self):
        self.assert_unique_field(self.model, "name", self.object.name)

    def test_name_required(self):
        self.assert_required_field(self.object, "name")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_category_name_saved_correctly(self):
        self.assert_model_instance(self.object, "name", self.object.name)

    def test_slug_auto_generated(self):
        self.assert_slug_auto_generation(self.object, "slug")

    def test_object_is_instance_of_category(self):
        self.assertIsInstance(self.object, self.model)
