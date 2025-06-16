from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from tests.utils.helpers import create_valid_test_image

User = get_user_model()


class TestRegisterAPI(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("register_api")
        cls.image = create_valid_test_image()
        cls.data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "image": cls.image,
            "password": "StrongPass123!",
            "password_confirm": "StrongPass123!",
        }

    def test_successful_registration(self):
        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="john@example.com").exists())

    def test_password_mismatch(self):
        self.data["password_confirm"] = self.data["password"] + "_mismatch"
        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password_confirm", response.data)

    def test_missing_fields(self):
        response = self.client.post(self.url, {}, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("first_name", response.data)
        self.assertIn("last_name", response.data)
        self.assertIn("email", response.data)

    def test_existing_email(self):
        User.objects.create_user(
            email="john@example.com", password="TestPass123!"
        )  # nosec
        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_veak_password(self):
        self.data["password"] = "weak"  # nosec
        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)

    def test_image_upload_with_invalid_content_and_txt_extension(self):
        invalid_image = SimpleUploadedFile(
            name="test_image.txt",
            content=b"not an image",
            content_type="text/plain",
        )
        self.data["image"] = invalid_image

        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("image", response.data)

    def test_empty_image_upload(self):
        empty_image = SimpleUploadedFile(
            name="empty_image.jpg",
            content=b"",
            content_type="image/jpeg",
        )
        self.data["image"] = empty_image

        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("image", response.data)

    def test_large_image_upload(self):
        large_image = SimpleUploadedFile(
            name="large_image.jpg",
            content=b"0" * (5 * 1024 * 1024),  # 5 MB
            content_type="image/jpeg",
        )
        self.data["image"] = large_image

        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("image", response.data)

    def test_disallowed_image_extension_with_invalid_content(self):
        invalid_image = SimpleUploadedFile(
            name="test_image.webp",
            content=b"not an image",
            content_type="image/webp",
        )
        self.data["image"] = invalid_image

        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("image", response.data)

    def test_disallowed_image_extension_with_valid_image(self):
        valid_image = create_valid_test_image()
        invalid_image = SimpleUploadedFile(
            name="test_image.webp",
            content=valid_image.read(),
            content_type="image/webp",
        )
        self.data["image"] = invalid_image

        response = self.client.post(self.url, self.data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("image", response.data)
