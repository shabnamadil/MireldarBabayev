from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.urls import reverse
from django.utils import timezone

from apps.blog.models import Blog
from apps.seo.models import BlogDetailPageSeo
from tests.utils.factories import BlogFactory, IPFactory, UserFactory
from tests.utils.helpers import BaseValidationTest, _ImageValidationTest


class TestBlogModelIntegration(BaseValidationTest, _ImageValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = BlogFactory
        cls.object = cls.factory()
        cls.model = Blog
        cls.image_field = "image"

    def test_title_max_length(self):
        self.assert_max_length(self.object, "title", 100)

    def test_short_description_max_length(self):
        self.assert_max_length(self.object, "short_description", 200)

    def test_status_max_length(self):
        self.assert_min_length(self.object, "status", 2)

    def test_slug_max_length(self):
        self.assert_max_length(self.object, "slug", 500)

    def test_title_unique(self):
        self.assert_unique_field(self.model, "title", self.object.title)

    def test_title_required(self):
        self.assert_required_field(self.object, "title")

    def test_short_description_required(self):
        self.assert_required_field(self.object, "short_description")

    def test_content_required(self):
        self.assert_required_field(self.object, "content")

    def test_image_required(self):
        self.assert_required_field(self.object, "image")

    def test_category_required(self):
        self.object.category.set([])
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_author_required(self):
        self.assert_required_field(self.object, "author")

    def test_status_required(self):
        self.assert_required_field(self.object, "status")

    def test_raises_validation_error_when_invalid_status_choices(
        self,
    ):
        blog = self.factory.build(status="invalid_status")
        with self.assertRaises(ValidationError):
            blog.full_clean()

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_blog_title_saved_correctly(self):
        self.assert_model_instance(self.object, "title", self.object.title)

    def test_blog_short_description_saved_correctly(self):
        self.assert_model_instance(
            self.object, "short_description", self.object.short_description
        )

    def test_blog_content_saved_correctly(self):
        self.assert_model_instance(self.object, "content", self.object.content)

    def test_blog_image_saved_correctly(self):
        self.assertTrue(self.object.image.name.startswith("blogs/"))
        self.assertTrue(self.object.image.name.endswith(".jpg"))

    def test_blog_category_saved_correctly(self):
        self.assert_model_instance(self.object, "category", self.object.category)

    def test_category_count(self):
        self.assertEqual(self.object.category.count(), 1)

    def test_category_remove(self):
        self.object.category.set([])
        self.assertEqual(self.object.category.count(), 0)

    def test_tag_saved_correctly(self):
        self.assert_model_instance(self.object, "tag", self.object.tag)

    def test_tag_count(self):
        self.assertEqual(self.object.tag.count(), 1)

    def test_tag_remove(self):
        self.object.tag.set([])
        self.assertEqual(self.object.tag.count(), 0)

    def test_blog_author_saved_correctly(self):
        self.assert_model_instance(self.object, "author", self.object.author)

    def test_author_deletion_deletes_blog(self):
        self.object.author.delete()
        self.assertEqual(Blog.objects.count(), 0)

    def test_blog_author_persistence(self):
        user = UserFactory()
        blog = BlogFactory(author=user)
        self.assertEqual(blog.author, user)

    def test_blog_status_saved_correctly(self):
        self.assert_model_instance(self.object, "status", self.object.status)

    def test_slug_auto_generated(self):
        self.assert_slug_auto_generation(self.object, "slug")

    def test_object_is_instance_of_blog(self):
        self.assertIsInstance(self.object, self.model)

    def test_blogs_are_ordered_by_published_at_desc(self):
        self.assert_ordering(self.factory, self.model, "published_at")

    def test_creating_blog_also_creates_related_seo_instance(self):
        seo_instance = BlogDetailPageSeo.objects.filter(blog=self.object)
        self.assertTrue(seo_instance.exists())

    def test_creating_second_blog_detail_page_seo_raises_integrity_error(
        self,
    ):
        with self.assertRaises(IntegrityError):
            BlogDetailPageSeo.objects.create(blog=self.object)

    def test_deleting_blog_also_deletes_related_seo_instance(self):
        deleted_blog_object = self.object.delete()
        seo_instance = BlogDetailPageSeo.objects.filter(
            blog=deleted_blog_object
        ).first()
        self.assertIsNone(seo_instance)

    def test_viewed_ips_initally_empty(self):
        self.assertEqual(self.object.viewed_ips.count(), 0)

    def test_viewed_ips_addition(self):
        ip1 = IPFactory(view_ip="192.168.1.1")
        ip2 = IPFactory(view_ip="10.0.0.1")

        self.object.viewed_ips.add(ip1, ip2)
        self.assertEqual(self.object.viewed_ips.count(), 2)
        self.assertIn(ip1, self.object.viewed_ips.all())

    def test_increment_view_count_adds_ip_and_increments(self):
        ip = IPFactory(view_ip="123.123.123.123")
        self.object.increment_view_count(ip)

        self.object.refresh_from_db()
        self.assertEqual(self.object.view_count, 1)
        self.assertIn(ip, self.object.viewed_ips.all())

    def test_increment_view_count_does_not_duplicate_ip_or_increment(self):
        ip = IPFactory(view_ip="123.123.123.123")

        self.object.increment_view_count(ip)
        self.object.refresh_from_db()
        self.assertEqual(self.object.view_count, 1)

        self.object.increment_view_count(ip)
        self.object.refresh_from_db()
        self.assertEqual(self.object.view_count, 1)

    def test_view_count_initially_zero(self):
        self.assertEqual(self.object.view_count, 0)

    def test_view_count_increments(self):
        ip = IPFactory(view_ip="123.123.123.123")
        self.object.increment_view_count(ip)
        self.object.refresh_from_db()
        self.assertEqual(self.object.view_count, 1)

    def test_blog_default_status_is_published(self):
        self.assertEqual(self.object.status, Blog.Status.PUBLISHED)

    def test_blog_status_changes(self):
        self.object.status = Blog.Status.DRAFT
        self.object.save()
        self.assertEqual(self.object.status, Blog.Status.DRAFT)

    def test_published_at_auto_set(self):
        """Test that published_at is set when status is PUBLISHED."""
        self.assertIsNotNone(self.object.published_at)
        self.assertTrue(
            timezone.now() - self.object.published_at < timedelta(seconds=5)
        )

    def test_published_date_returns_correct_format(self):
        dt = timezone.now()
        blog = BlogFactory(published_at=dt)
        expected = timezone.localtime(dt).strftime("%d %b, %Y")
        self.assertEqual(blog.published_date, expected)

    def test_get_absolute_url(self):
        url = self.object.get_absolute_url()
        expected_url = reverse("blog-detail", args=[self.object.slug])
        self.assertEqual(url, expected_url)

    def test_published_blog_manager_returns_only_published(self):
        BlogFactory(status=Blog.Status.DRAFT)
        result = Blog.published.all()
        self.assertEqual(result.count(), 1)

    def test_sitemap_image_property(self):
        self.assertEqual(self.object.sitemap_image, self.object.image.url)
