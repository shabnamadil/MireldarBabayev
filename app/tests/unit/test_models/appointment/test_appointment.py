from django.utils import timezone
from django.utils.timezone import timedelta
from django.core.exceptions import ValidationError

from utils.tests.base import BaseValidationTest
from apps.appointment.models import Appointment, Timetable
from apps.appointment.forms import AppointmentForm


class TestAppointmentModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.timetable = Timetable.objects.create(
            start_time=timezone.now() + timedelta(hours=1),
            end_time=timezone.now() + timedelta(days=1)
        )

        cls.appointment = Appointment.objects.create(
            full_name='Test user',
            phone='+994776577887',
            location='Test location',
            message='Test message',
            available_time=cls.timetable
        )

    @classmethod
    def get_invalid_form_data(cls, time):
        """Return invalid form data for testing."""
        return {
            'full_name': 'Test user',
            'phone': '+994776577887',
            'location': 'Test location',
            'message': 'Test message',
            'available_time': time.id
        }

    def test_str_method(self):
        self.assert_str_method(self.appointment, f'Test user - {self.appointment.available_time}')

    def test_fields_max_length(self):
        self.assert_max_length(self.appointment, 'full_name', 100)
        self.assert_max_length(self.appointment, 'phone', 17)
        self.assert_max_length(self.appointment, 'location', 200)

    def test_object_count(self):
        self.assert_object_count(Appointment, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(Appointment)

    def test_model(self):
        self.assert_model_instance(Appointment, 'full_name', 'Test user')
        self.assert_model_instance(Appointment, 'phone', '+994776577887')
        self.assert_model_instance(Appointment, 'location', 'Test location')
        self.assert_model_instance(Appointment, 'message', 'Test message')
        self.assert_model_instance(Appointment, 'available_time', self.timetable)

    def test_number(self):
        self.assert_invalid_number(self.appointment, number_field='phone')

    def test_missing_full_name(self):
        """Test missing full_name should raise an error."""
        appointment = Appointment(
            phone="1234567890",
            available_time=self.timetable
        )
        with self.assertRaises(ValidationError):
            appointment.full_clean()

    def test_missing_phone(self):
        """Test missing full_name should raise an error."""
        appointment = Appointment(
            full_name="Test name",
            available_time=self.timetable
        )
        with self.assertRaises(ValidationError):
            appointment.full_clean()

    def test_missing_available_time(self):
        """Test missing full_name should raise an error."""
        appointment = Appointment(
            full_name='Test full name',
            phone="1234567890"
        )
        with self.assertRaises(ValidationError):
            appointment.full_clean()

    def test_unique_available_time(self):
        self.assert_unique_field(Appointment, 'available_time', self.timetable)

    def test_start_time_in_past(self):
        """Test validation error when start_time is in the past"""
        invalid_available_time = Timetable.objects.create(
            start_time=timezone.now() - timedelta(hours=1),
            end_time=timezone.now() + timedelta(days=1)
        )

        form = AppointmentForm(data=self.get_invalid_form_data(invalid_available_time))

        self.assertFalse(form.is_valid())
        self.assertIn('available_time', form.errors)

    def test_end_time_before_start_time(self):
        """Test validation error when end_time is before start_time"""
        invalid_available_time = Timetable.objects.create(
            start_time=timezone.now() + timedelta(hours=1),
            end_time=timezone.now() - timedelta(days=1)
        )

        form = AppointmentForm(data=self.get_invalid_form_data(invalid_available_time))
        self.assertFalse(form.is_valid())
        self.assertIn('available_time', form.errors)


    def test_missing_start_time(self):
        """Test validation error when start_time is missing"""
        invalid_available_time = Timetable(
            end_time=timezone.now() + timedelta(days=1)
        )

        form = AppointmentForm(data=self.get_invalid_form_data(invalid_available_time))

        self.assertFalse(form.is_valid())
        self.assertIn('available_time', form.errors)


    def test_missing_end_time(self):
        """Test validation error when end_time is missing"""
        invalid_available_time = Timetable(
            start_time=timezone.now() + timedelta(days=1)
        )
        
        form = AppointmentForm(data=self.get_invalid_form_data(invalid_available_time))

        self.assertFalse(form.is_valid())
        self.assertIn('available_time', form.errors)
