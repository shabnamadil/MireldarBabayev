from apps.blog.models import IP
from tests.utils.helpers import BaseValidationTest


class TestIPModel(BaseValidationTest):

    def test_ip_str_returns_ip(self):
        self.assert_str_output(IP, "view_ip", "192.168.1.1")
