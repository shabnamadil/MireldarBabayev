from django.core.exceptions import ValidationError


class _MapUrlValidationTest:
    """
    Abstract class for work hours validation tests.
    Do not run directly.
    """

    object = None
    map_url_field = None

    def test_valid_google_map_url(self):
        self.object.map_url = "https://www.google.com/maps/embed?pb=!1m18!..."
        try:
            self.object.full_clean()
        except ValidationError:
            self.fail("ValidationError raised unexpectedly on valid URL.")

    def test_invalid_google_map_url_http(self):
        self.object.map_url = "http://www.google.com/maps/embed?pb=!1m18!..."
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_invalid_google_map_url_wrong_domain(self):
        self.object.map_url = "https://maps.google.com/embed?pb=!1m18!..."
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_invalid_google_map_url_missing_embed(self):
        self.object.map_url = "https://www.google.com/maps?q=location"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_invalid_google_map_url_random_text(self):
        self.object.map_url = "just some random text"
        with self.assertRaises(ValidationError):
            self.object.full_clean()
