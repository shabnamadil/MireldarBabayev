from django.core.exceptions import ValidationError

from apps.blog.models import IP
from tests.utils.factories import IPFactory
from tests.utils.helpers import (
    BaseValidationTest,
)


class TestIPModelIntegration(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = IPFactory
        cls.object = cls.factory()
        cls.model = IP

    def test_view_ip_required(self):
        field = IP._meta.get_field("view_ip")
        field.editable = True
        self.assert_required_field(self.object, "view_ip")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_ip_view_ip_saved_correctly(self):
        self.assert_model_instance(self.object, "view_ip", self.object.view_ip)

    def test_object_is_instance_of_ip(self):
        self.assertIsInstance(self.object, self.model)

    def test_ip_change_view_ip_raises_validation_error(self):
        obj = self.factory.create(view_ip="192.168.1.2")

        obj.view_ip = "10.0.0.1"

        with self.assertRaises(ValidationError):
            obj.save()
