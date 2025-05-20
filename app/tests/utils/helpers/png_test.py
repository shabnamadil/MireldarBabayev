from django.core.files.uploadedfile import SimpleUploadedFile

from tests.utils.helpers import BaseDataMixin, generate_png_file


class _PngValidationTest(BaseDataMixin):
    """
    Abstract class for PNG validation tests.
    Do not run directly.
    """

    object = None

    def test_raises_validation_error_with_invalid_png_content_and_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name="invalid_png.jpg",
            content=b"not an png at all",
            content_type="image/jpeg",
        )
        self.assert_invalid_data(self.object, "png", fake_file)

    def test_raises_validation_error_with_invalid_png_content_valid_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name="invalid_png.png",
            content=b"not an png at all",
            content_type="image/png",
        )
        self.assert_invalid_data(self.object, "png", fake_file)

    def test_raises_validation_error_with_valid_data_invalid_png_extension(
        self,
    ):
        png_file = generate_png_file()
        fake_file = SimpleUploadedFile(
            name="valid_png.jpg",
            content=png_file.read(),
            content_type="image/jpeg",
        )
        self.assert_invalid_data(self.object, "png", fake_file)

    def test_raises_validation_error_with_empty_png(self):
        fake_file = SimpleUploadedFile(
            name="empty.png",
            content=b"",
            content_type="image/png",
        )
        self.assert_invalid_data(self.object, "png", fake_file)

    def test_raises_validation_error_with_empty_data_invalid_extension(self):
        fake_file = SimpleUploadedFile(
            name="empty.jpg",
            content=b"",
            content_type="image/jpeg",
        )
        self.assert_invalid_data(self.object, "png", fake_file)

    def test_raises_validation_error_when_invalid_png_size(self):
        png_file = generate_png_file()
        content = png_file.read()
        large_content = content * ((5 * 1024 * 1024) // len(content) + 1)
        fake_file = SimpleUploadedFile(
            name="large_png.png",
            content=large_content,
            content_type="image/png",
        )
        self.assert_invalid_data(self.object, "png", fake_file)
