from tests.utils.helpers import BaseDataMixin


class _VideoIdValidationtest(BaseDataMixin):
    """
    Abstract class for Video ID validation tests.
    Do not run directly.
    """

    video_id_field = None
    object = None

    def test_invalid_video_id_too_short(self):
        short_video_id = "shortID"
        self.assert_invalid_data(self.object, self.video_id_field, short_video_id)

    def test_invalid_video_id_with_invalid_chars(self):
        invalid_video_id = "invalid@ID!"
        self.assert_invalid_data(self.object, self.video_id_field, invalid_video_id)
