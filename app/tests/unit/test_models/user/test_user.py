from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

from utils.tests.base import BaseValidationTest

User = get_user_model()


class TestCustomUserModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            first_name='Test',
            last_name='User',
            password='123',
            email='test@gmail.com',
            image=SimpleUploadedFile(
            "test1.jpg", 
            b"dummy png content", 
            content_type="image/jpeg"
            ),
        )

    def test_str_method(self):
        return self.assert_str_method(self.user, 'test@gmail.com')

    def test_fields_max_length(self):
        self.assert_max_length(self.user, 'first_name', 30)
        self.assert_max_length(self.user, 'last_name', 30)
    
    def test_email_unique(self):
        self.assert_unique_field(User, 'email', 'test@gmail.com')

    def test_object_count(self):
        self.assert_object_count(User, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(User)

    def test_get_full_name(self):
        return self.assertEqual(self.user.full_name, 'Test User')
    
    def test_admin_user_name(self):
        self.user.first_name = ''
        self.user.last_name = ''
        self.user.save()
        self.assertEqual(self.user.full_name, 'Admin User')

    def test_model(self):
        self.assert_model_instance(User, 'first_name', 'Test')
        self.assert_model_instance(User, 'last_name', 'User')
        self.assert_model_instance(User, 'email', 'test@gmail.com')
        self.assert_model_instance(User, 'first_name', 'Test')
        self.assertNotEqual(User, 'password', '123')
        self.assertTrue(self.user.image.name.startswith('users/'))
        self.assertTrue(self.user.image.name.endswith('jpg'))


    def test_email_required(self):
        new_user = User(
            first_name='New',
            last_name='User',
            password='123'
        )
        
        with self.assertRaises(ValidationError):
            new_user.full_clean()

    def test_password_hashed(self):
        """Test that the password is hashed and not stored in plain text."""
        self.assertTrue(check_password('123', self.user.password))  # Ensure it's hashed correctly
