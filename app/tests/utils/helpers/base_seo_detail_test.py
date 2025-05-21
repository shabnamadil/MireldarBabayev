class BaseSeoDetailPageTest:
    """
    Abstract test mixin for SEO Detail page models with common fields and behaviors.

    This class defines reusable tests for SEO detail model fields (meta_description,
    meta_keywords, og_description) and behaviors (singleton,
    required fields). It is not a TestCase subclass, so Django's test runner ignores
    it, ensuring tests only run in subclasses.
    """

    model = None
    object = None

    def test_meta_description_max_length(self):
        self.assert_max_length(self.object, "meta_description", 160)

    def test_meta_keywords_max_length(self):
        self.assert_max_length(self.object, "meta_keywords", 160)

    def test_og_description_max_length(self):
        self.assert_max_length(self.object, "og_description", 160)

    def test_meta_description_min_length(self):
        self.assert_min_length(self.object, "meta_description", 50)

    def test_meta_keywords_min_length(self):
        self.assert_min_length(self.object, "meta_keywords", 50)

    def test_og_description_min_length(self):
        self.assert_min_length(self.object, "og_description", 50)

    def test_meta_description_required(self):
        self.assert_required_field(self.object, "meta_description")

    def test_meta_keywords_required(self):
        self.assert_required_field(self.object, "meta_keywords")

    def test_og_description_required(self):
        self.assert_required_field(self.object, "og_description")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_object_is_instance_of_model(self):
        self.assertIsInstance(self.object, self.model)

    def test_meta_description_saved_correctly(self):
        self.assert_model_instance(
            self.object, "meta_description", self.object.meta_description
        )

    def test_meta_keywords_saved_correctly(self):
        self.assert_model_instance(
            self.object, "meta_keywords", self.object.meta_keywords
        )

    def test_og_description_saved_correctly(self):
        self.assert_model_instance(
            self.object, "og_description", self.object.og_description
        )
