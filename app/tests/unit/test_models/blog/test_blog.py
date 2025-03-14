from datetime import timedelta

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.utils import timezone

from apps.blog.models import IP, Blog, Category, Tag
from utils.helpers.slugify import custom_slugify
from utils.tests.base import BaseValidationTest


class TestBlogModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.category = Category.objects.create(name='Test category')
        cls.tag = Tag.objects.create(name='Test tag')
        cls.blog = Blog.objects.create(
            title='Test blog',
            short_description='Test description',
            content='Test content',
            image=SimpleUploadedFile(
                "test1.jpg", b"dummy jpg content", content_type="image/jpeg"
            ),
            author=cls.user,
        )
        cls.blog.category.add(cls.category)
        cls.blog.tag.add(cls.tag)

    def test_str_method(self):
        self.assert_str_method(self.blog, 'Test blog')

    def test_model(self):
        self.assert_model_instance(Blog, 'title', 'Test blog')
        self.assert_model_instance(
            Blog, 'short_description', 'Test description'
        )
        self.assert_model_instance(Blog, 'content', 'Test content')
        self.assert_model_instance(Blog, 'author', self.user)
        self.assertTrue(self.blog.image.name.startswith('blogs/'))
        self.assertTrue(self.blog.image.name.endswith('jpg'))

    def test_object_count(self):
        self.assert_object_count(Blog, 1)

    def test_deletion(self):
        self.assert_object_deleted(Blog)

    def test_unique_title(self):
        self.assert_unique_field(Blog, 'title', 'Test blog')

    def test_fields_max_length(self):
        self.assert_max_length(self.blog, 'title', 100)
        self.assert_max_length(self.blog, 'short_description', 200)
        self.assert_max_length(self.blog, 'slug', 500)

    def test_category_count(self):
        self.assertEqual(self.blog.category.count(), 1)

    def test_category_remove(self):
        self.blog.category.remove(self.category)
        self.assertEqual(self.blog.category.count(), 0)

    def test_tag_count(self):
        self.assertEqual(self.blog.tag.count(), 1)

    def test_tag_remove(self):
        self.blog.tag.remove(self.tag)
        self.assertEqual(self.blog.tag.count(), 0)

    def test_slug_auto_generation(self):
        """Test that the slug is auto-generated using custom_slugify."""
        expected_slug = custom_slugify(self.blog.title)
        self.assertEqual(self.blog.slug, expected_slug)

    def test_slug_on_object_edit(self):
        self.blog.title = 'Edited blog title'
        self.blog.save()
        expected_slug = custom_slugify(self.blog.title)
        self.assertNotEqual(self.blog.slug, expected_slug)

    def test_blog_ordering(self):
        """Ensure blogs are ordered by 'created_at' descending."""
        new_blog = Blog.objects.create(
            title='New blog',
            short_description='Test description',
            content='Test content',
            image='blog/1.jpg',
            author=self.user,
        )

        blogs = Blog.objects.all()
        self.assertEqual(blogs.first(), new_blog)
        self.assertEqual(blogs.last(), self.blog)

    def test_published_at_auto_set(self):
        """Test that published_at is set when status is PUBLISHED."""
        self.assertIsNotNone(self.blog.published_at)
        self.assertTrue(
            timezone.now() - self.blog.published_at < timedelta(seconds=5)
        )

    def test_published_date_property(self):
        local_time = timezone.localtime(self.blog.published_at)
        formatted_date = local_time.strftime('%d %b, %Y')
        self.assertEqual(self.blog.published_date, formatted_date)

    def test_get_absolute_url(self):
        url = self.blog.get_absolute_url()
        expected_url = reverse('blog-detail', args=[self.blog.slug])
        self.assertEqual(url, expected_url)

    def test_sitemap_image_property(self):
        self.assertEqual(self.blog.sitemap_image, self.blog.image.url)

    def test_initial_view_count(self):
        self.assertEqual(self.blog.view_count, 0)

    def test_increment_view_count(self):
        """Test that increment_view_count adds a unique IP and increments view_count."""
        initial_view_count = self.blog.view_count
        ip_instance = IP.objects.create(view_ip="192.168.1.1")
        self.blog.increment_view_count(ip_instance)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.view_count, initial_view_count + 1)
        self.assertEqual(self.blog.viewed_ips.count(), initial_view_count + 1)

        # Try to add the same IP again; view_count should not change.
        self.blog.increment_view_count(ip_instance)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.view_count, initial_view_count + 1)

    def test_viewed_ips_field_editable(self):
        """Test that the 'viewed_ips' field is marked as not editable."""
        field = Blog._meta.get_field('viewed_ips')
        self.assertFalse(field.editable)

    def test_view_count_field_editable(self):
        """Test that the 'viewed_ips' field is marked as not editable."""
        field = Blog._meta.get_field('view_count')
        self.assertFalse(field.editable)

    def test_initial_status(self):
        self.assertEqual(self.blog.status, self.blog.Status.PUBLISHED)

    def test_status_change(self):
        self.blog.status = self.blog.Status.DRAFT
        self.blog.save()
        self.assertNotEqual(self.blog.status, self.blog.Status.PUBLISHED)
