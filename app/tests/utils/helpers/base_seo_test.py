from tests.utils.helpers import BaseSeoDetailPageTest


class BaseSeoPageTest(BaseSeoDetailPageTest):
    """
    Abstract test mixin for SEO page models with common fields and behaviors.

    This class defines reusable tests for SEO fields (meta_title, meta_description,
    meta_keywords, og_title, og_description, og_image) and behaviors (singleton,
    required fields). It is not a TestCase subclass, so Django's test runner ignores
    it, ensuring tests only run in subclasses.
    """

    def test_meta_title_max_length(self):
        self.assert_max_length(self.object, "meta_title", 60)

    def test_og_title_max_length(self):
        self.assert_max_length(self.object, "og_title", 60)

    def test_meta_title_min_length(self):
        self.assert_min_length(self.object, "meta_title", 30)

    def test_og_title_min_length(self):
        self.assert_min_length(self.object, "og_title", 30)

    def test_singleton(self):
        self.assert_singleton(self.model)

    def test_meta_title_required(self):
        self.assert_required_field(self.object, "meta_title")

    def test_og_title_required(self):
        self.assert_required_field(self.object, "og_title")

    def test_og_description_required(self):
        self.assert_required_field(self.object, "og_description")

    def test_meta_title_saved_correctly(self):
        self.assert_model_instance(self.object, "meta_title", self.object.meta_title)

    def test_og_title_saved_correctly(self):
        self.assert_model_instance(self.object, "og_title", self.object.og_title)

    def test_og_image_saved_correctly(self):
        self.assertTrue(self.object.og_image.name.startswith("seo-images/"))
        self.assertTrue(self.object.og_image.name.endswith(".jpg"))

    def test_object_saved_without_image_correctly(self):
        self.object.og_image = None
        self.object.save()
        self.assertIsNone(self.object.og_image.name)
        self.assertIsInstance(self.object, self.model)
