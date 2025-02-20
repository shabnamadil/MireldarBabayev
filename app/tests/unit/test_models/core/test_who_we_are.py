from apps.core.models import WhoWeAre
from utils.tests.base import BaseValidationTest


class WhoWeAreModelTest(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.data = WhoWeAre.objects.create(
            title='Test title',
            video_link='https://www.youtube.com/watch?v=U4fHv1KXQkY',
            content='Test content'
        )

    def test_str_method(self):
        self.assert_str_method(self.data, 'Biz kimik?')

    def test_model(self):
        self.assert_model_instance(WhoWeAre, 'title', 'Test title')
        self.assert_model_instance(WhoWeAre, 'video_link', 'https://www.youtube.com/watch?v=U4fHv1KXQkY')
        self.assert_model_instance(WhoWeAre, 'content', 'Test content')

    def test_title_max_length(self):
        self.assert_max_length(self.data, 'title', 50)

    def test_video_link_type(self):
        self.assert_field_type(self.data, 'video_link', 'https://invalid/')

    def test_model_singleton(self):
        self.assert_singleton(WhoWeAre)

    def test_object_count(self):
        self.assert_object_count(WhoWeAre, 1)

    def test_deletion(self):
        self.assert_object_deleted(WhoWeAre)