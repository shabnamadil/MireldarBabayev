from django.core.exceptions import ValidationError

from apps.blog.models import IP
from utils.tests.base import BaseValidationTest


class TestIPModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.ip = IP.objects.create(view_ip="127.0.0.1")

    def test_str_method(self):
        self.assert_str_method(self.ip, self.ip.view_ip)

    def test_model(self):
        self.assert_model_instance(IP, "view_ip", self.ip.view_ip)

    def test_ip_field_editable_false(self):
        self.ip.view_ip = "192.168.1.1"
        with self.assertRaises(ValidationError):
            self.ip.save()

    def test_object_count(self):
        self.assert_object_count(IP, 1)

    def test_deletion(self):
        self.assert_object_deleted(IP)

    def test_invalid_ip(self):
        """Ensure that invalid IPs raise a ValidationError."""
        invalid_ips = [
            "999.999.999.999",  # Out of range values
            "abc.def.ghi.jkl",  # Non-numeric
            "192.168.1.256",  # Invalid octet (256 > 255)
            "192.168.1.-1",  # Negative number
            "192.168.1.1.1",  # Too many octets
            "2001:db8:::1",  # Invalid IPv6
            "2001:db8:zzzz::1",  # Invalid characters in IPv6
        ]
        for ip in invalid_ips:
            obj = IP(view_ip=ip)
            with self.assertRaises(ValidationError):
                obj.full_clean()
