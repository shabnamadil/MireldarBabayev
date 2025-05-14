from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core.files.uploadedfile import SimpleUploadedFile

from tests.utils.factories import UserFactory
from tests.utils.helpers import create_valid_test_image
from utils.tests.base import BaseValidationTest

User = get_user_model()


class TestCustomUserModelIntegration(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()

    def test_first_name_max_length(self):
        self.assert_max_length(self.user, 'first_name', 30)

    def test_last_name_max_length(self):
        self.assert_max_length(self.user, 'last_name', 30)

    def test_email_unique(self):
        self.assert_unique_field(User, 'email', 'test@gmail.com')

    def test_invalid_email_raises_validation_error(self):
        self.assert_invalid_email(self.user)

    def test_email_required(self):
        self.assert_required_field(self.user, 'email')

    def test_first_name_required(self):
        self.assert_required_field(self.user, 'first_name')

    def test_last_name_required(self):
        self.assert_required_field(self.user, 'last_name')

    def test_password_required(self):
        self.assert_required_field(self.user, 'password')

    def test_object_count(self):
        self.assert_object_count(User, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(User)

    def test_user_first_name_saved_correctly(self):
        self.assert_model_instance(self.user, 'first_name', 'John')

    def test_user_last_name_saved_correctly(self):
        self.assert_model_instance(self.user, 'last_name', 'Doe')

    def test_user_email_saved_correctly(self):
        self.assert_model_instance(self.user, 'email', 'test@gmail.com')

    def test_user_image_saved_correctly(self):
        self.assertTrue(self.user.image.name.startswith('users/'))

    def test_user_image_extension(self):
        self.assertTrue(self.user.image.name.endswith('.jpg'))

    def test_user_password_is_hashed(self):
        self.assertTrue(check_password('testpassword', self.user.password))
        self.assertNotEqual(self.user.password, 'testpassword')

    def test_object_is_instance_of_user(self):
        self.assertIsInstance(self.user, User)

    def test_raises_validation_error_when_invalid_image_uploaded_with_disallowed_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name='invalid_image.txt',
            content=b'not an image at all',
            content_type='text/plain',
        )
        self.assert_invalid_image(self.user, 'image', fake_file)

    def test_raises_validation_error_when_empty_txt_file_uploaded(self):
        fake_file = SimpleUploadedFile(
            name='empty_image.txt', content=b'', content_type='text/plain'
        )
        self.assert_invalid_image(self.user, 'image', fake_file)

    def test_raises_validation_error_when_empty_image_uploaded(self):
        fake_file = SimpleUploadedFile(
            name='empty_image.jpg', content=b'', content_type='image/jpeg'
        )
        self.assert_invalid_image(self.user, 'image', fake_file)

    def test_raises_validation_error_when_invalid_image_uploaded_with_valid_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name='invalid_image.jpg',
            content=b'not an image at all',
            content_type='image/jpeg',
        )
        self.assert_invalid_image(self.user, 'image', fake_file)

    def test_raises_validation_error_when_valid_image_uploaded_with_disallowed_txt_extension(
        self,
    ):
        image = create_valid_test_image()
        fake_file = SimpleUploadedFile(
            name='valid_image.txt', content=image.read(), content_type='text/plain'
        )
        self.assert_invalid_image(self.user, 'image', fake_file)

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
            self.assert_invalid_image(self.user, 'image', fake_file)

    def test_raises_validation_error_when_invalid_image_size(self):
        fake_file = SimpleUploadedFile(
            name='large_image.jpg',
            content=b'0' * (5 * 1024 * 1024 + 1),  # 5MB + 1 byte
            content_type='image/jpeg',
        )
        self.assert_invalid_image(self.user, 'image', fake_file)
