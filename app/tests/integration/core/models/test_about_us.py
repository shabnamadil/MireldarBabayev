from apps.core.models import AboutUs
from tests.utils.factories import AboutUsFactory
from tests.utils.helpers import (
    BaseValidationTest,
    _ImageValidationTest,
    _VideoIdValidationtest,
)


class TestAboutUsModelIntegration(
    BaseValidationTest, _ImageValidationTest, _VideoIdValidationtest
):
    @classmethod
    def setUpTestData(cls):
        cls.factory = AboutUsFactory
        cls.object = cls.factory()
        cls.model = AboutUs
        cls.image_field = "image"
        cls.video_id_field = "video_id"

    def test_video_id_max_length(self):
        self.assert_max_length(self.object, "video_id", 11)

    def test_image_required(self):
        self.assert_required_field(self.object, "image")

    def test_video_id_required(self):
        self.assert_required_field(self.object, "video_id")

    def test_content_required(self):
        self.assert_required_field(self.object, "content")

    def test_mission_required(self):
        self.assert_required_field(self.object, "mission")

    def test_vision_required(self):
        self.assert_required_field(self.object, "vision")

    def test_value_required(self):
        self.assert_required_field(self.object, "value")

    def test_video_id_unique(self):
        self.assert_unique_field(self.model, "video_id", self.object.video_id)

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_singleton(self):
        self.assert_singleton(self.model)

    def test_image_saved_correctly(self):
        self.assertTrue(self.object.image.name.startswith("about/"))
        self.assertTrue(self.object.image.name.endswith(".jpg"))

    def test_video_id_saved_correctly(self):
        self.assert_model_instance(self.object, "video_id", self.object.video_id)

    def test_content_saved_correctly(self):
        self.assert_model_instance(self.object, "content", self.object.content)

    def test_mission_saved_correctly(self):
        self.assert_model_instance(self.object, "mission", self.object.mission)

    def test_vision_saved_correctly(self):
        self.assert_model_instance(self.object, "vision", self.object.vision)

    def test_value_saved_correctly(self):
        self.assert_model_instance(self.object, "value", self.object.value)

    def test_object_is_instance_of_about_us(self):
        self.assertIsInstance(self.object, self.model)
