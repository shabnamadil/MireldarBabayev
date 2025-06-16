from django.templatetags.static import static

from apps.user.api.serializers import UserInfoSerializer
from rest_framework.test import APIRequestFactory, APITestCase
from tests.utils.factories import UserFactory


class TestUserInfoSerializer(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.user_factory = UserFactory
        cls.serializer = UserInfoSerializer

    def test_user_with_image_and_request(self):
        user = self.user_factory(image="profile.png")
        request = self.factory.get("/")
        serializer = self.serializer(user, context={"request": request})
        data = serializer.data
        self.assertTrue(data["image"].endswith("/profile.png"))
        self.assertEqual(data["image"], request.build_absolute_uri(user.image.url))
        self.assertEqual(data["email"], user.email)
        self.assertEqual(data["full_name"], user.get_full_name())

    def test_user_with_image_without_request(self):
        user = self.user_factory(image="profile.png")
        serializer = self.serializer(user, context={})
        data = serializer.data
        self.assertEqual(data["image"], user.image.url)

    def test_user_without_image_with_request(self):
        user = self.user_factory(image=None)
        request = self.factory.get("/")
        serializer = self.serializer(user, context={"request": request})
        data = serializer.data
        self.assertEqual(
            data["image"],
            request.build_absolute_uri(static("images/user.png")),
        )

    def test_user_without_image_and_request(self):
        user = self.user_factory(image=None)
        serializer = self.serializer(user, context={})
        data = serializer.data
        self.assertEqual(data["image"], static("images/user.png"))
