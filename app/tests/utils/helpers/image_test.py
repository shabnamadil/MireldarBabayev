from django.core.files.uploadedfile import SimpleUploadedFile

from tests.utils.helpers import BaseDataMixin, create_valid_test_image


class _ImageValidationTest(BaseDataMixin):
    """
    Abstract class for IMAGE validation tests.
    Do not run directly.
    """

    image_field = None
    object = None

    def test_raises_validation_error_when_invalid_image_uploaded_with_disallowed_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name="invalid_image.txt",
            content=b"not an image at all",
            content_type="text/plain",
        )
        self.assert_invalid_data(self.object, self.image_field, fake_file)

    def test_raises_validation_error_when_empty_txt_file_uploaded(self):
        fake_file = SimpleUploadedFile(
            name="empty_image.txt", content=b"", content_type="text/plain"
        )
        self.assert_invalid_data(self.object, self.image_field, fake_file)

    def test_raises_validation_error_when_empty_image_uploaded(self):
        fake_file = SimpleUploadedFile(
            name="empty_image.jpg", content=b"", content_type="image/jpeg"
        )
        self.assert_invalid_data(self.object, self.image_field, fake_file)

    def test_raises_validation_error_when_invalid_image_uploaded_with_valid_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name="invalid_image.jpg",
            content=b"not an image at all",
            content_type="image/jpeg",
        )
        self.assert_invalid_data(self.object, self.image_field, fake_file)

    def test_raises_validation_error_when_valid_image_uploaded_with_disallowed_txt_extension(
        self,
    ):
        image = create_valid_test_image()
        fake_file = SimpleUploadedFile(
            name="valid_image.txt",
            content=image.read(),
            content_type="text/plain",
        )
        self.assert_invalid_data(self.object, self.image_field, fake_file)

    def test_raises_validation_error_when_valid_image_uploaded_with_disallowed_image_extensions(
        self,
    ):
        image = create_valid_test_image()
        disallowed_extentions = ["webp", "jpf", "xpm"]
        for ext in disallowed_extentions:
            fake_file = SimpleUploadedFile(
                name=f"valid_image.{ext}",
                content=image.read(),
                content_type=f"image/{ext}",
            )
            self.assert_invalid_data(self.object, self.image_field, fake_file)

    def test_raises_validation_error_when_invalid_image_size(self):
        image = create_valid_test_image()
        content = image.read()
        large_content = content * ((5 * 1024 * 1024) // len(content) + 1)
        fake_file = SimpleUploadedFile(
            name="large_image.jpg",
            content=large_content,
            content_type="image/jpeg",
        )
        self.assert_invalid_data(self.object, self.image_field, fake_file)
