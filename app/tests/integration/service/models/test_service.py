from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.service.models import Service
from tests.utils.factories import ServiceFactory
from tests.utils.helpers import create_valid_test_image, generate_png_file
from utils.tests.base import BaseValidationTest


class TestServiceModelIntegration(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.service = ServiceFactory()

    def test_name_max_length(self):
        self.assert_max_length(self.service, 'name', 30)

    def test_short_description_max_length(self):
        self.assert_max_length(self.service, 'short_description', 160)

    def test_short_description_min_length(self):
        self.assert_min_length(self.service, 'short_description', 145)

    def test_title_max_length(self):
        self.assert_max_length(self.service, 'title', 60)

    def test_title_min_length(self):
        self.assert_min_length(self.service, 'title', 30)

    def test_content_max_length(self):
        self.assert_max_length(self.service, 'content', 1000)

    def test_content_min_length(self):
        self.assert_min_length(self.service, 'content', 300)

    def test_slug_max_length(self):
        self.assert_max_length(self.service, 'slug', 500)

    def test_title_unique(self):
        self.assert_unique_field(Service, 'title', self.service.title)

    def test_name_unique(self):
        self.assert_unique_field(Service, 'name', self.service.name)

    def test_name_required(self):
        self.assert_required_field(self.service, 'name')

    def test_short_description_required(self):
        self.assert_required_field(self.service, 'short_description')

    def test_png_required(self):
        self.assert_required_field(self.service, 'png')

    def test_image_required(self):
        self.assert_required_field(self.service, 'image')

    def test_title_required(self):
        self.assert_required_field(self.service, 'title')

    def test_content_required(self):
        self.assert_required_field(self.service, 'content')

    def test_background_color_required(self):
        self.assert_required_field(self.service, 'background_color')

    def test_raises_validation_error_when_invalid_background_color_choices(self):
        service = ServiceFactory.build(background_color='invalid_color')
        with self.assertRaises(ValidationError):
            service.full_clean()

    def test_object_count(self):
        self.assert_object_count(Service, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(Service)

    def test_service_name_saved_correctly(self):
        self.assert_model_instance(self.service, 'name', self.service.name)

    def test_service_short_description_saved_correctly(self):
        self.assert_model_instance(
            self.service, 'short_description', self.service.short_description
        )

    def test_service_png_saved_correctly(self):
        self.assertTrue(self.service.png.name.startswith('services/png/'))
        self.assertTrue(self.service.png.name.endswith('.png'))

    def test_service_image_saved_correctly(self):
        self.assertTrue(self.service.image.name.startswith('services/images/'))
        self.assertTrue(self.service.image.name.endswith('.jpg'))

    def test_service_title_saved_correctly(self):
        self.assert_model_instance(self.service, 'title', self.service.title)

    def test_service_content_saved_correctly(self):
        self.assert_model_instance(self.service, 'content', self.service.content)

    def test_service_background_color_saved_correctly(self):
        self.assert_model_instance(
            self.service, 'background_color', self.service.background_color
        )

    def test_slug_auto_generated(self):
        self.assert_slug_auto_generation(self.service, 'slug')

    def test_object_is_instance_of_service(self):
        self.assertIsInstance(self.service, Service)

    def test_raises_validation_error_with_invalid_png_content_and_extension(self):
        fake_file = SimpleUploadedFile(
            name='invalid_png.jpg',
            content=b'not an png at all',
            content_type='image/jpeg',
        )
        self.assert_invalid_image(self.service, 'png', fake_file)

    def test_raises_validation_error_with_invalid_png_content_valid_extension(self):
        fake_file = SimpleUploadedFile(
            name='invalid_png.png',
            content=b'not an png at all',
            content_type='image/png',
        )
        self.assert_invalid_image(self.service, 'png', fake_file)

    def test_raises_validation_error_with_valid_data_invalid_png_extension(self):
        png_file = generate_png_file()
        fake_file = SimpleUploadedFile(
            name='valid_png.jpg',
            content=png_file.read(),
            content_type='image/jpeg',
        )
        self.assert_invalid_image(self.service, 'png', fake_file)

    def test_raises_validation_error_with_empty_png(self):
        fake_file = SimpleUploadedFile(
            name='empty.png',
            content=b'',
            content_type='image/png',
        )
        self.assert_invalid_image(self.service, 'png', fake_file)

    def test_raises_validation_error_with_empty_data_invalid_extension(self):
        fake_file = SimpleUploadedFile(
            name='empty.jpg',
            content=b'',
            content_type='image/jpeg',
        )
        self.assert_invalid_image(self.service, 'png', fake_file)

    def test_raises_validation_error_when_invalid_png_size(self):
        png_file = generate_png_file()
        content = png_file.read()
        large_content = content * ((5 * 1024 * 1024) // len(content) + 1)
        fake_file = SimpleUploadedFile(
            name='large_png.png',
            content=large_content,
            content_type='image/png',
        )
        self.assert_invalid_image(self.service, 'png', fake_file)

    def test_raises_validation_error_when_invalid_image_uploaded_with_disallowed_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name='invalid_image.txt',
            content=b'not an image at all',
            content_type='text/plain',
        )
        self.assert_invalid_image(self.service, 'image', fake_file)

    def test_raises_validation_error_when_empty_txt_file_uploaded(self):
        fake_file = SimpleUploadedFile(
            name='empty_image.txt', content=b'', content_type='text/plain'
        )
        self.assert_invalid_image(self.service, 'image', fake_file)

    def test_raises_validation_error_when_empty_image_uploaded(self):
        fake_file = SimpleUploadedFile(
            name='empty_image.jpg', content=b'', content_type='image/jpeg'
        )
        self.assert_invalid_image(self.service, 'image', fake_file)

    def test_raises_validation_error_when_invalid_image_uploaded_with_valid_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name='invalid_image.jpg',
            content=b'not an image at all',
            content_type='image/jpeg',
        )
        self.assert_invalid_image(self.service, 'image', fake_file)

    def test_raises_validation_error_when_valid_image_uploaded_with_disallowed_txt_extension(
        self,
    ):
        image = create_valid_test_image()
        fake_file = SimpleUploadedFile(
            name='valid_image.txt', content=image.read(), content_type='text/plain'
        )
        self.assert_invalid_image(self.service, 'image', fake_file)

    def test_raises_validation_error_when_valid_image_uploaded_with_disallowed_image_extensions(
        self,
    ):
        image = create_valid_test_image()
        disallowed_extentions = ['webp', 'jpf', 'xpm']
        for ext in disallowed_extentions:
            fake_file = SimpleUploadedFile(
                name=f'valid_image.{ext}',
                content=image.read(),
                content_type=f'image/{ext}',
            )
            self.assert_invalid_image(self.service, 'image', fake_file)

    def test_raises_validation_error_when_invalid_image_size(self):
        image = create_valid_test_image()
        content = image.read()
        large_content = content * ((5 * 1024 * 1024) // len(content) + 1)
        fake_file = SimpleUploadedFile(
            name='large_image.jpg',
            content=large_content,
            content_type='image/jpeg',
        )
        self.assert_invalid_image(self.service, 'image', fake_file)
