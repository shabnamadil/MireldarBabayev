from django.contrib.auth import get_user_model

from utils.tests.base import BaseValidationTest

User = get_user_model()


class TestCustomUserModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.model = User

    def test_user_str_returns_email(self):
        return self.assert_str_output(self.model, 'email', 'test@gmail.com')

    def test_full_name_returns_combined_name(self):
        user = self.model(first_name='Test', last_name='User')
        self.assertEqual(user.full_name, 'Test User')

    def test_full_name_fallback_when_no_first_and_last_name(self):
        user = self.model()
        self.assertEqual(user.full_name, 'Admin User')

    def test_full_name_fallback_when_no_last_name(self):
        user = self.model(first_name="Jhon")
        self.assertEqual(user.full_name, 'Jhon')

    def test_full_name_fallback_when_no_first_name(self):
        user = self.model(last_name="Doe")
        self.assertEqual(user.full_name, 'Doe')

    def test_username_field_is_email(self):
        assert self.model.USERNAME_FIELD == 'email'

    def test_required_fields_are_empty(self):
        assert self.model.REQUIRED_FIELDS == []
