from apps.blog.models import Blog
from tests.utils.helpers import BaseValidationTest


class TestBlogModel(BaseValidationTest):

    def test_blog_str_returns_title(self):
        self.assert_str_output(Blog, "title", "Test Blog Title")

    def test_viewed_ips_field_editable(self):
        """Test that the 'viewed_ips' field is marked as not editable."""
        field = Blog._meta.get_field("viewed_ips")
        self.assertFalse(field.editable)

    def test_view_count_field_editable(self):
        """Test that the 'view_count' field is marked as not editable."""
        field = Blog._meta.get_field("view_count")
        self.assertFalse(field.editable)
