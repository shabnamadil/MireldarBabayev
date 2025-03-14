from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError

from apps.blog.models import Blog
from apps.seo.models import BlogDetailPageSeo
from utils.tests.seo import BaseValidationTest


class TestBlogDetailPageSeoModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.model = BlogDetailPageSeo

        cls.blog, _ = Blog.objects.get_or_create(
            title='Test blog',
            short_description='Test description',
            content='Test content',
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01",
                content_type="image/jpeg",
            ),
            author=cls.user,
        )

        cls.valid_data = {
            "meta_description": "This is a valid meta description within the required length range.",
            "meta_keywords": "keyword1, keyword2, keyword3, keyword4",
            "og_description": "This is a valid OG description for testing SEO constraints.",
        }

        cls.instance, created = BlogDetailPageSeo.objects.get_or_create(
            blog=cls.blog
        )

        for key, value in cls.valid_data.items():
            setattr(cls.instance, key, value)
        cls.instance.save()

    def test_str_method(self):
        self.assert_str_method(self.instance, f'SEO ==> {self.blog}')

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_fields_min_length(self):
        self.assert_min_length(self.instance, "meta_description", 50)
        self.assert_min_length(self.instance, "meta_keywords", 50)
        self.assert_min_length(self.instance, "og_description", 50)

        with self.assertRaises(ValidationError) as cm:
            self.instance.full_clean()

        errors = cm.exception.message_dict
        self.assertIn("meta_description", errors)
        self.assertIn("meta_keywords", errors)
        self.assertIn("og_description", errors)

    def test_fields_max_length(self):
        self.assert_max_length(self.instance, "meta_description", 160)
        self.assert_max_length(self.instance, "meta_keywords", 160)
        self.assert_max_length(self.instance, "og_description", 160)

        with self.assertRaises(ValidationError) as cm:
            self.instance.full_clean()

        errors = cm.exception.message_dict
        self.assertIn("meta_description", errors)
        self.assertIn("meta_keywords", errors)
        self.assertIn("og_description", errors)

    def test_model(self):
        self.assert_model_instance(
            BlogDetailPageSeo,
            'meta_description',
            self.valid_data["meta_description"],
        )
        self.assert_model_instance(
            BlogDetailPageSeo,
            'meta_keywords',
            self.valid_data["meta_keywords"],
        )
        self.assert_model_instance(
            BlogDetailPageSeo,
            'og_description',
            self.valid_data["og_description"],
        )
        self.assert_model_instance(BlogDetailPageSeo, 'blog', self.blog)

    def test_automatically_created_blog_detail_page_seo(self):
        blog = Blog.objects.create(
            title='Test blog new',
            short_description='Test description new',
            content='Test content new',
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01",
                content_type="image/jpeg",
            ),
            author=self.user,
        )

        deteail_page_seo_instance = BlogDetailPageSeo.objects.get(blog=blog)

        self.assertEqual(deteail_page_seo_instance, blog.detail_page_seo)

    def test_unique_object_for_each_blog(self):
        blog = Blog.objects.first()

        with self.assertRaises(IntegrityError):
            BlogDetailPageSeo.objects.create(blog=blog)
