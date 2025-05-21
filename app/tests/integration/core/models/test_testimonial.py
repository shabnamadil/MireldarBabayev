from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.core.models import Testimoinal
from tests.utils.factories import TestimonialFactory
from tests.utils.helpers import (
    BaseValidationTest,
    _ImageValidationTest,
)


class TestTestimonialModelIntegration(BaseValidationTest, _ImageValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = TestimonialFactory
        cls.object = cls.factory()
        cls.model = Testimoinal
        cls.image_field = "client_image"

    def test_contact_str_returns_valid_string(self):
        expected = _("Comment by %(client_full_name)s") % {
            "client_full_name": self.object.client_full_name
        }
        self.assertEqual(str(self.object), expected)

    def test_client_full_name_max_length(self):
        self.assert_max_length(self.object, "client_full_name", 20)

    def test_client_profession_max_length(self):
        self.assert_max_length(self.object, "client_profession", 100)

    def test_client_comment_max_length(self):
        self.assert_max_length(self.object, "client_comment", 155)

    def test_client_comment_min_length(self):
        self.assert_min_length(self.object, "client_comment", 150)

    def test_client_image_required(self):
        self.assert_required_field(self.object, "client_image")

    def test_client_full_name_required(self):
        self.assert_required_field(self.object, "client_full_name")

    def test_client_profession_required(self):
        self.assert_required_field(self.object, "client_profession")

    def test_client_comment_required(self):
        self.assert_required_field(self.object, "client_comment")

    def test_star_required(self):
        self.assert_required_field(self.object, "star")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_client_image_saved_correctly(self):
        self.assertTrue(self.object.client_image.name.startswith("testimonials/"))
        self.assertTrue(self.object.client_image.name.endswith(".jpg"))

    def test_client_full_name_saved_correctly(self):
        self.assert_model_instance(
            self.object, "client_full_name", self.object.client_full_name
        )

    def test_client_profession_saved_correctly(self):
        self.assert_model_instance(
            self.object, "client_profession", self.object.client_profession
        )

    def test_client_comment_saved_correctly(self):
        self.assert_model_instance(
            self.object, "client_comment", self.object.client_comment
        )

    def test_star_saved_correctly(self):
        self.assert_model_instance(self.object, "star", self.object.star)

    def test_object_is_instance_of_testimonial(self):
        self.assertIsInstance(self.object, self.model)

    def test_testimonials_are_ordered_by_created_at_desc(self):
        self.assert_ordering(self.factory, self.model)

    def test_valid_star_values(self):
        for value in range(1, 6):  # 1 through 5 inclusive
            obj = self.factory.build(star=value)
            try:
                obj.full_clean()  # Should not raise
            except ValidationError:
                self.fail(f"Value {value} should be valid for star")

    def test_invalid_star_values(self):
        for value in [0, 6, -1, 100]:
            obj = self.factory.build(star=value)
            with self.assertRaises(ValidationError):
                obj.full_clean()

    def test_star_range_property(self):
        self.object.star = 3
        expected_range = range(3)
        self.assertEqual(list(self.object.star_range), list(expected_range))
