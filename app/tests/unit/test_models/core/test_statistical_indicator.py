from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.core.models.statistics import StatisticalIndicator
from utils.tests.base import BaseValidationTest


class TestStatisticalIndicatorModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.indicator = StatisticalIndicator.objects.create(
            png=SimpleUploadedFile(
            "test1.png", 
            b"dummy png content", 
            content_type="image/png"
            ),
            value=10,
            name='Test'
        )

    def test_statistical_indicator_model(self):
        self.assert_model_instance(StatisticalIndicator, 'value', 10)
        self.assert_model_instance(StatisticalIndicator, 'name', 'Test')
        self.assertTrue(self.indicator.png.name.startswith('statistics/'))
        self.assertTrue(self.indicator.png.name.endswith('png'))
        
    def test_str_method(self):
        self.assert_str_method(self.indicator, 'Test')

    def test_statistical_indicator_png_extension(self):
        statistical_indicator = self.indicator
        statistical_indicator.png = 'statistics/test.jpg'
        with self.assertRaises(ValidationError):
            statistical_indicator.full_clean()

    def test_statistical_indicator_value_type(self):
        self.assert_field_type(self.indicator, 'value', 'a')

    def test_statistical_indicator_name_max_length(self):
        self.assert_max_length(self.indicator, 'name', 50)

    def test_statistical_indicator_name_unique(self):
        self.assert_unique_field(StatisticalIndicator, 'name', 'Test')
    
    def test_object_count(self):
        self.assert_object_count(StatisticalIndicator, 1)

    def test_deletion(self):
        self.assert_object_deleted(StatisticalIndicator)