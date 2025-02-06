from utils.tests.base import BaseValidationTest

from apps.blog.models import Category
from utils.helpers.slugify import custom_slugify


class TestCategoryModel(BaseValidationTest):
    
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Test Category')

    def test_str_method(self):
        self.assert_str_method(self.category, self.category.name)

    def test_model(self):
        self.assert_model_instance(Category, 'name', self.category.name)
        self.assert_model_instance(Category, 'slug', custom_slugify(self.category.name))

    def test_object_count(self):
        self.assert_object_count(Category, 1)

    def test_deletion(self):
        self.assert_object_deleted(Category)

    def test_unique_name(self):
        self.assert_unique_field(Category, 'name', self.category.name)

    def test_name_max_length(self):
        self.assert_max_length(self.category, 'name', 150)

    def test_slug_max_length(self):
        self.assert_max_length(self.category, 'slug', 500)

    def test_slug_on_object_edit(self):
        self.category.name = 'Edited Category'
        self.category.save()
        self.assertNotEqual(self.category.slug, custom_slugify(self.category.name))
        self.assertEqual(self.category.slug, 'test-category')