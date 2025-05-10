from django.contrib.auth import get_user_model

from utils.tests.base import BaseValidationTest

User = get_user_model()


class TestCustomUserModel(BaseValidationTest):

    def test_user_str_returns_email(self):
        return self.assert_str_output(User, 'email', 'test@gmail.com')

    def test_full_name_returns_combined_name(self):
        user = User(first_name='Test', last_name='User')
        self.assertEqual(user.full_name, 'Test User')

    def test_full_name_fallback_when_no_first_and_last_name(self):
        user = User()
        self.assertEqual(user.full_name, 'Admin User')

    def test_full_name_fallback_when_no_last_name(self):
        user = User(first_name="Jhon")
        self.assertEqual(user.full_name, 'Jhon')

    def test_full_name_fallback_when_no_first_name(self):
        user = User(last_name="Doe")
        self.assertEqual(user.full_name, 'Doe')

    def test_username_field_is_email(self):
        assert User.USERNAME_FIELD == 'email'

    def test_required_fields_are_empty(self):
        assert User.REQUIRED_FIELDS == []
