from io import BytesIO

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


def create_test_image():
    buffer = BytesIO()
    image = Image.new('RGB', (100, 100), color='blue')
    image.save(buffer, format='JPEG')
    buffer.seek(0)
    return SimpleUploadedFile(
        'avatar.jpg', buffer.read(), content_type='image/jpeg'
    )


class TestRegisterAPI(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('register_api')
        cls.image = create_test_image()
        cls.data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "image": cls.image,
            "password": "StrongPass123!",
            "password_confirm": "StrongPass123!",
        }

    def test_successful_registration(self):
        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="john@example.com").exists())

    def test_password_mismatch(self):
        self.data["password_confirm"] = "DifferentPass123!"
        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password_confirm', response.data)

    def test_missing_fields(self):
        response = self.client.post(self.url, {}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('first_name', response.data)
        self.assertIn('last_name', response.data)
        self.assertIn('email', response.data)

    def test_existing_email(self):
        User.objects.create_user(
            email="john@example.com", password="TestPass123!"
        )
        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_veak_password(self):
        self.data["password"] = "weak"
        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_invalid_image_upload(self):
        invalid_image = SimpleUploadedFile(
            name='test_image.txt',
            content=b'not an image',  # Not valid image data
            content_type='text/plain',
        )
        self.data["image"] = invalid_image

        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('image', response.data)
