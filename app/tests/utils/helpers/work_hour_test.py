from django.core.exceptions import ValidationError


class _WorkHourValidationTest:
    """
    Abstract class for work hours validation tests.
    Do not run directly.
    """

    object = None
    work_hour_field = None

    def test_valid_work_hours(self):
        self.object.work_hours = "09:00 - 17:00"
        try:
            self.object.full_clean()
        except ValidationError as e:
            print(e)
            self.fail("ValidationError raised unexpectedly!")

    def test_invalid_format(self):
        self.object.work_hours = "0900 - 1700"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_invalid_hour_range(self):
        self.object.work_hours = "25:00 - 30:00"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_invalid_minute_range(self):
        self.object.work_hours = "09:60 - 17:00"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_start_time_greater_than_end_time(self):
        self.object.work_hours = "18:00 - 09:00"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_start_time_equals_end_time(self):
        self.object.work_hours = "10:00 - 10:00"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_missing_leading_zero(self):
        self.object.work_hours = "9:00 - 10:00"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_missing_space(self):
        self.object.work_hours = "10:00-10:00"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_missing_left_space(self):
        self.object.work_hours = "10:00 -10:00"
        with self.assertRaises(ValidationError):
            self.object.full_clean()

    def test_wrong_seperator(self):
        self.object.work_hours = "10:00 / 10:00"
        with self.assertRaises(ValidationError):
            self.object.full_clean()
