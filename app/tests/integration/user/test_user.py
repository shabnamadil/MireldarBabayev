from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from utils.tests.base import BaseValidationTest

from ..factories.user_factory import UserFactory

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

    def test_custom_user_manager_creates_user(self):
        self.assertIsInstance(self.user, User)

    def test_custom_user_manager_creates_superuser(self):
        superuser = User.objects.create_superuser(
            email='admin@example.com', password='adminpass'
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_user_is_not_superuser_by_default(self):
        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)

    def test_create_super_user_raises_value_error_when_no_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email=None)

    def test_create_super_user_raises_validation_error_when_invalid_email(
        self,
    ):
        superuser = User.objects.create_superuser(email='test')
        self.assert_invalid_email(superuser)

    def test_create_super_user_raises_validation_error_when_no_password(self):
        superuser = User.objects.create_superuser(
            email='testuser@gmail.com', password=None
        )
        with self.assertRaises(ValidationError):
            superuser.full_clean()

    def test_create_super_user_raises_integrity_error_when_duplicate_email(
        self,
    ):
        with self.assertRaises(IntegrityError):
            User.objects.create_superuser(
                email='test@gmail.com', password='testpassword'
            )
