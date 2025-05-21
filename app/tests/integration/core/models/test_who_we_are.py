from apps.core.models import WhoWeAre
from tests.utils.factories import WhoWeAreFactory
from tests.utils.helpers import (
    BaseValidationTest,
    _VideoIdValidationtest,
)


class TestWhoWeAreModelIntegration(BaseValidationTest, _VideoIdValidationtest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = WhoWeAreFactory
        cls.object = cls.factory()
        cls.model = WhoWeAre
        cls.video_id_field = "video_link"

    def test_title_max_length(self):
        self.assert_max_length(self.object, "title", 50)

    def test_video_link_max_length(self):
        self.assert_max_length(self.object, "video_link", 11)

    def test_title_required(self):
        self.assert_required_field(self.object, "title")

    def test_video_link_required(self):
        self.assert_required_field(self.object, "video_link")

    def test_content_required(self):
        self.assert_required_field(self.object, "content")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_singleton(self):
        self.assert_singleton(self.model)

    def test_title_saved_correctly(self):
        self.assert_model_instance(self.object, "title", self.object.title)

    def test_video_link_saved_correctly(self):
        self.assert_model_instance(self.object, "video_link", self.object.video_link)

    def test_content_saved_correctly(self):
        self.assert_model_instance(self.object, "content", self.object.content)

    def test_object_is_instance_of_who_we_are(self):
        self.assertIsInstance(self.object, self.model)
