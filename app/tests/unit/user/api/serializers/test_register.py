from io import BytesIO

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.user.api.serializers import RegisterSerializer
from PIL import Image

User = get_user_model()


def create_test_image():
    buffer = BytesIO()
    image = Image.new('RGB', (100, 100), color='red')
    image.save(buffer, format='JPEG')
    buffer.seek(0)
    return SimpleUploadedFile(
        'test.jpg', buffer.read(), content_type='image/jpeg'
    )


class TestRegisterSerializer(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.image = create_test_image()
        cls.data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "image": cls.image,
            "password": "StrongPass123!",
            "password_confirm": "StrongPass123!",
        }

    def test_valid_register_serializer_data_creates_user(self):
        serializer = RegisterSerializer(data=self.data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertTrue(User.objects.filter(email="john@example.com").exists())
        self.assertTrue(user.check_password("StrongPass123!"))

    def test_invalid_image_upload_raises_error(self):
        invalid_image = SimpleUploadedFile(
            name='test_image.txt',
            content=b'not an image',  # Not valid image data
            content_type='text/plain',
        )
        self.data["image"] = invalid_image

        serializer = RegisterSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('image', serializer.errors)

    def test_missing_password_confirm(self):
        self.data["password_confirm"] = None
        serializer = RegisterSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password_confirm", serializer.errors)

    def test_passwords_do_not_match(self):
        self.data["password_confirm"] = "DifferentPass123!"
        serializer = RegisterSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password_confirm", serializer.errors)

    def test_weak_password(self):
        self.data["password"] = "123"
        self.data["password_confirm"] = "123"
        serializer = RegisterSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_missing_required_fields(self):
        self.data["first_name"] = None
        self.data["last_name"] = None
        self.data["email"] = None
        serializer = RegisterSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())
        for field in ["first_name", "last_name", "email"]:
            with self.subTest(field=field):
                self.assertIn(field, serializer.errors)

    def test_email_already_registered(self):
        User.objects.create_user(
            email="john@example.com", password="SomePass123!"
        )
        serializer = RegisterSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_password_confirm_not_saved_in_user_model(self):
        serializer = RegisterSerializer(data=self.data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertFalse(hasattr(user, "password_confirm"))
