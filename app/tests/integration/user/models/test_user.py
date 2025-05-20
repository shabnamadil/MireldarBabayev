from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from tests.utils.factories import UserFactory
from tests.utils.helpers import BaseValidationTest, _ImageValidationTest

User = get_user_model()


class TestCustomUserModelIntegration(BaseValidationTest, _ImageValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.object = UserFactory()
        cls.image_field = "image"
        cls.model = User

    def test_first_name_max_length(self):
        self.assert_max_length(self.object, "first_name", 30)

    def test_last_name_max_length(self):
        self.assert_max_length(self.object, "last_name", 30)

    def test_email_unique(self):
        self.assert_unique_field(self.model, "email", self.object.email)

    def test_invalid_email_raises_validation_error(self):
        self.assert_invalid_email(self.object)

    def test_email_required(self):
        self.assert_required_field(self.object, "email")

    def test_first_name_required(self):
        self.assert_required_field(self.object, "first_name")

    def test_last_name_required(self):
        self.assert_required_field(self.object, "last_name")

    def test_password_required(self):
        self.assert_required_field(self.object, "password")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_user_first_name_saved_correctly(self):
        self.assert_model_instance(self.object, "first_name", self.object.first_name)

    def test_user_last_name_saved_correctly(self):
        self.assert_model_instance(self.object, "last_name", self.object.last_name)

    def test_user_email_saved_correctly(self):
        self.assert_model_instance(self.object, "email", self.object.email)

    def test_user_image_saved_correctly(self):
        self.assertTrue(self.object.image.name.startswith("users/"))

    def test_user_image_extension(self):
        self.assertTrue(self.object.image.name.endswith(".jpg"))

    def test_user_password_is_hashed(self):
        self.assertTrue(check_password("testpassword", self.object.password))
        self.assertNotEqual(self.object.password, "testpassword")

    def test_object_is_instance_of_user(self):
        self.assertIsInstance(self.object, self.model)
