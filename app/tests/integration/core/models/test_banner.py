from apps.core.models import Banner
from tests.utils.factories import BannerFactory
from tests.utils.helpers import (
    BaseValidationTest,
    _PngValidationTest,
    _VideoIdValidationtest,
)


class TestAboutUsModelIntegration(
    BaseValidationTest, _PngValidationTest, _VideoIdValidationtest
):
    @classmethod
    def setUpTestData(cls):
        cls.factory = BannerFactory
        cls.object = cls.factory()
        cls.model = Banner
        cls.png_field = "png"
        cls.video_id_field = "video_id"

    def test_title_max_length(self):
        self.assert_max_length(self.object, "title", 100)

    def test_subtitle_max_length(self):
        self.assert_max_length(self.object, "subtitle", 100)

    def test_video_id_max_length(self):
        self.assert_max_length(self.object, "video_id", 11)

    def test_title_required(self):
        self.assert_required_field(self.object, "title")

    def test_subtitle_required(self):
        self.assert_required_field(self.object, "subtitle")

    def test_description_required(self):
        self.assert_required_field(self.object, "description")

    def test_png_required(self):
        self.assert_required_field(self.object, "png")

    def test_title_unique(self):
        self.assert_unique_field(self.model, "title", self.object.title)

    def test_subtitle_unique(self):
        self.assert_unique_field(self.model, "subtitle", self.object.subtitle)

    def test_description_unique(self):
        self.assert_unique_field(self.model, "description", self.object.description)

    def test_video_id_unique(self):
        self.assert_unique_field(self.model, "video_id", self.object.video_id)

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_title_saved_correctly(self):
        self.assert_model_instance(self.object, "title", self.object.title)

    def test_subtitle_saved_correctly(self):
        self.assert_model_instance(self.object, "subtitle", self.object.subtitle)

    def test_description_saved_correctly(self):
        self.assert_model_instance(self.object, "description", self.object.description)

    def test_png_saved_correctly(self):
        self.assertTrue(self.object.png.name.startswith("banner/"))
        self.assertTrue(self.object.png.name.endswith(".png"))

    def test_video_id_saved_correctly(self):
        self.assert_model_instance(self.object, "video_id", self.object.video_id)

    def test_object_is_instance_of_banner(self):
        self.assertIsInstance(self.object, self.model)

    def test_banners_are_ordered_by_created_at_desc(self):
        self.assert_ordering(self.factory, self.model)
