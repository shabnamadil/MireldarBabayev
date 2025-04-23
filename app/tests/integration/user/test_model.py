from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

from tests.factories.user_factory import UserFactory
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
        user = UserFactory.build(email=None)
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_first_name_required(self):
        user = UserFactory.build(first_name=None)
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_last_name_required(self):
        user = UserFactory.build(last_name=None)
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_password_required(self):
        user = UserFactory.build(password=None)
        with self.assertRaises(ValidationError):
            user.full_clean()

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
