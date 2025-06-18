from django.urls import reverse_lazy

from apps.blog.models import Blog
from tests.utils.factories import BlogFactory, BlogsPageSeoFactory, CommentFactory
from tests.utils.helpers import BaseValidationTest


class TestBlogListView(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse_lazy("blogs")
        cls.model = Blog

        cls.seo = BlogsPageSeoFactory.create()
        cls.blog1 = BlogFactory.create(view_count=100)
        cls.blog2 = BlogFactory.create(view_count=50)

        CommentFactory.create_batch(3, blog=cls.blog1)
        CommentFactory.create_batch(1, blog=cls.blog2)

    def test_response_status_code(self):
        self.assert_status_code(self.url)

    def test_correct_template_used(self):
        self.assert_template_used(self.url, "components/blog/blog-list.html")

    def test_blog_list_view_context_contains_popular_blogs(self):
        response = self.client.get(self.url)
        self.assertIn("popular_blogs", response.context)

    def test_blogs_count_in_context(self):
        response = self.client.get(self.url)
        popular_blogs = response.context["popular_blogs"]
        self.assertEqual(len(popular_blogs), 2)

    def test_blogs_count_limit_in_context(self):
        BlogFactory.create_batch(6)
        response = self.client.get(self.url)
        popular_blogs = response.context["popular_blogs"]
        self.assertEqual(len(popular_blogs), 3)

    def test_view_with_no_blogs(self):
        self.assert_view_without_context_data(self.model, self.url, "popular_blogs")

    def test_draft_blogs_not_in_context(self):
        draft_blog = BlogFactory.create(status=Blog.Status.DRAFT)
        response = self.client.get(self.url)
        popular_blog_ids = [b.id for b in response.context["popular_blogs"]]
        self.assertNotIn(draft_blog.id, popular_blog_ids)

    def test_only_published_blogs_in_context(self):
        published_blog = BlogFactory.create(status=Blog.Status.PUBLISHED)
        response = self.client.get(self.url)
        popular_blog_ids = [b.id for b in response.context["popular_blogs"]]
        self.assertIn(published_blog.id, popular_blog_ids)

    def test_popular_blogs_ordering(self):
        response = self.client.get(self.url)
        popular_blogs = response.context["popular_blogs"]

        # Expected order: blog1 (3 comments, 100 views), blog2 (1 comment, 50 views)
        self.assertEqual(popular_blogs[0], self.blog1)
        self.assertEqual(popular_blogs[1], self.blog2)

    def test_categories_in_context(self):
        # 2 blog items created in setup
        response = self.client.get(self.url)
        self.assertIn("categories", response.context)
        self.assertEqual(len(response.context["categories"]), 2)

    def test_tags_in_context(self):
        # 2 blog items created in setup
        response = self.client.get(self.url)
        self.assertIn("tags", response.context)
        self.assertEqual(len(response.context["tags"]), 2)

    def test_blog_list_view_context_seo(self):
        response = self.client.get(self.url)
        self.assertIn("seo", response.context)
        self.assertEqual(response.context["seo"], self.seo)

    def test_blog_list_view_context_seo_none_when_missing(self):
        self.seo.delete()

        response = self.client.get(self.url)

        self.assertIn("seo", response.context)
        self.assertIsNone(response.context["seo"])
