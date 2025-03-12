from django.utils import timezone
from django.utils.timezone import timedelta

from apps.appointment.forms import TimetableForm
from apps.appointment.models import Timetable
from utils.tests.base import BaseValidationTest


class TestTimeTableModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.start_time = timezone.now() + timedelta(minutes=15)
        cls.end_time = cls.start_time + timedelta(hours=1)

        cls.timetable = Timetable.objects.create(
            start_time=cls.start_time,
            end_time=cls.end_time,
        )

    def test_str_method(self):
        expected_str = f"{self.start_time.strftime('%d %b %Y, %H:%M')} - {self.end_time.strftime('%d %b %Y, %H:%M')}"
        self.assert_str_method(self.timetable, expected_str)

    def test_object_count(self):
        self.assert_object_count(Timetable, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(Timetable)

    def test_model(self):
        self.assert_model_instance(
            Timetable,
            "start_time",
            self.start_time,
        )
        self.assert_model_instance(Timetable, "end_time", self.end_time)

    def test_start_time_unique(self):
        object = Timetable.objects.first()
        self.assert_unique_field(
            Timetable,
            "start_time",
            object.start_time,
        )

    def test_end_time_unique(self):
        object = Timetable.objects.first()
        self.assert_unique_field(Timetable, "end_time", object.end_time)

    def test_valid_data(self):
        valid_form_data = {
            "start_time": self.start_time + timedelta(minutes=15),
            "end_time": self.end_time + timedelta(hours=1),
        }
        form = TimetableForm(data=valid_form_data)
        self.assertTrue(form.is_valid())

    def test_start_time_in_past(self):
        """Test validation error when start_time is in the past"""
        invalid_form_data = {
            "start_time": timezone.now() - timezone.timedelta(days=1),
            "end_time": self.end_time + timedelta(hours=1),
        }
        form = TimetableForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())

    def test_end_time_before_start_time(self):
        """Test validation error when end_time is before start_time"""
        invalid_form_data = {
            "start_time": timezone.now() + timezone.timedelta(days=1),
            "end_time": self.end_time - timedelta(hours=1),
        }
        form = TimetableForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())

    def test_missing_start_time(self):
        """Test validation error when start_time is missing"""
        form_data = {"end_time": timezone.now() + timedelta(hours=1)}
        form = TimetableForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_missing_end_time(self):
        """Test validation error when end_time is missing"""
        form_data = {"start_time": timezone.now()}
        form = TimetableForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_start_and_end_time_non_equiality(
        self,
    ):
        time = timezone.now()
        invalid_form_data = {
            "start_time": time,
            "end_time": time,
        }

        form = TimetableForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())
