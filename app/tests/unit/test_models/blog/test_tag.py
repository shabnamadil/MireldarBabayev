from apps.blog.models import Tag
from utils.helpers.slugify import custom_slugify
from utils.tests.base import BaseValidationTest


class TestTagModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name='Test Tag')

    def test_str_method(self):
        self.assert_str_method(self.tag, self.tag.name)

    def test_model(self):
        self.assert_model_instance(Tag, 'name', self.tag.name)
        self.assert_model_instance(Tag, 'slug', custom_slugify(self.tag.name))

    def test_object_count(self):
        self.assert_object_count(Tag, 1)

    def test_unique_name(self):
        self.assert_unique_field(Tag, 'name', 'Test Tag')

    def test_fields_max_length(self):
        self.assert_max_length(self.tag, 'name', 80)
        self.assert_max_length(self.tag, 'slug', 500)

    def test_slug_on_object_edit(self):
        self.tag.name = 'Edited Tag'
        self.tag.save()
        self.assertNotEqual(self.tag.slug, custom_slugify(self.tag.name))
        self.assertEqual(self.tag.slug, 'test-tag')

    def test_deletion(self):
        self.assert_object_deleted(Tag)
