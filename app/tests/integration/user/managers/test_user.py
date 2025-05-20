from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from tests.utils.factories import UserFactory
from utils.tests.base import BaseValidationTest

User = get_user_model()


class TestCustomUserManager(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.model = User

    def test_custom_user_manager_creates_user(self):
        self.assertIsInstance(self.user, self.model)

    def test_custom_user_manager_creates_superuser(self):
        superuser = self.model.objects.create_superuser(
            email="admin@example.com", password="adminpass"
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_user_is_not_superuser_by_default(self):
        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)

    def test_create_super_user_raises_value_error_when_no_email(self):
        with self.assertRaises(ValueError):
            self.model.objects.create_superuser(email=None)

    def test_create_super_user_raises_validation_error_when_invalid_email(
        self,
    ):
        superuser = self.model.objects.create_superuser(email="test")
        self.assert_invalid_email(superuser)

    def test_create_super_user_raises_validation_error_when_no_password(
        self,
    ):
        superuser = self.model.objects.create_superuser(
            email="testuser@gmail.com", password=None
        )
        with self.assertRaises(ValidationError):
            superuser.full_clean()

    def test_create_super_user_raises_integrity_error_when_duplicate_email(
        self,
    ):
        with self.assertRaises(IntegrityError):
            self.model.objects.create_superuser(
                email=self.user.email, password="testpassword"
            )
