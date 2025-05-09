# Generated by Django 4.2.17 on 2025-04-11 09:19

from django.db import migrations, models
import django.db.models.deletion
import utils.helpers.validate_phone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'start_time',
                    models.DateTimeField(
                        unique=True, verbose_name='Görüşün başlama vaxtı'
                    ),
                ),
                (
                    'end_time',
                    models.DateTimeField(
                        unique=True, verbose_name='Görüşün bitmə vaxtı'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Rezervasiya üçün uyğun vaxt',
                'verbose_name_plural': 'Rezervasiya üçün uyğun vaxtlar',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'full_name',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 100-dür.',
                        max_length=100,
                        verbose_name='Ad, Soyad',
                    ),
                ),
                (
                    'phone',
                    models.CharField(
                        help_text='Yalnız rəqəm daxil edin',
                        max_length=17,
                        validators=[
                            utils.helpers.validate_phone.validate_phone_value
                        ],
                        verbose_name='Əlaqə nömrəsi',
                    ),
                ),
                (
                    'location',
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name='Məkan',
                    ),
                ),
                (
                    'message',
                    models.TextField(
                        blank=True, null=True, verbose_name='Mesaj'
                    ),
                ),
                (
                    'available_time',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='appointment',
                        to='appointment.timetable',
                        verbose_name='Uyğun tarix',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Rezervasiya',
                'verbose_name_plural': 'Rezervasiyalar',
                'ordering': ('-created_at',),
                'indexes': [
                    models.Index(
                        fields=['created_at'],
                        name='appointment_created_1cd9a1_idx',
                    )
                ],
            },
        ),
    ]
