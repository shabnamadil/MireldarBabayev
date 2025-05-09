# Generated by Django 4.2.17 on 2025-04-11 09:19

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='WhyChooseUs',
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
                    'title',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=200,
                        unique=True,
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_az',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_en',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_ru',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'short_description',
                    models.TextField(unique=True, verbose_name='Qısa məlumat'),
                ),
                (
                    'short_description_az',
                    models.TextField(
                        null=True, unique=True, verbose_name='Qısa məlumat'
                    ),
                ),
                (
                    'short_description_en',
                    models.TextField(
                        null=True, unique=True, verbose_name='Qısa məlumat'
                    ),
                ),
                (
                    'short_description_ru',
                    models.TextField(
                        null=True, unique=True, verbose_name='Qısa məlumat'
                    ),
                ),
                (
                    'png',
                    models.FileField(
                        upload_to='why_choose_us/', verbose_name='PNG'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Nə üçün biz?',
                'verbose_name_plural': 'Nə üçün biz?',
                'ordering': ['-created_at'],
                'indexes': [
                    models.Index(
                        fields=['-created_at'],
                        name='service_why_created_66ac3f_idx',
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name='Service',
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
                    'name',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=200,
                        unique=True,
                        verbose_name='Servisin adı',
                    ),
                ),
                (
                    'name_az',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name='Servisin adı',
                    ),
                ),
                (
                    'name_en',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name='Servisin adı',
                    ),
                ),
                (
                    'name_ru',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name='Servisin adı',
                    ),
                ),
                (
                    'short_description',
                    models.TextField(
                        help_text='Kontentin uzunlu]u 145-160 aralığındadır.',
                        validators=[
                            django.core.validators.MinLengthValidator(145),
                            django.core.validators.MaxLengthValidator(160),
                        ],
                        verbose_name='Qısa məlumat',
                    ),
                ),
                (
                    'short_description_az',
                    models.TextField(
                        help_text='Kontentin uzunlu]u 145-160 aralığındadır.',
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(145),
                            django.core.validators.MaxLengthValidator(160),
                        ],
                        verbose_name='Qısa məlumat',
                    ),
                ),
                (
                    'short_description_en',
                    models.TextField(
                        help_text='Kontentin uzunlu]u 145-160 aralığındadır.',
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(145),
                            django.core.validators.MaxLengthValidator(160),
                        ],
                        verbose_name='Qısa məlumat',
                    ),
                ),
                (
                    'short_description_ru',
                    models.TextField(
                        help_text='Kontentin uzunlu]u 145-160 aralığındadır.',
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(145),
                            django.core.validators.MaxLengthValidator(160),
                        ],
                        verbose_name='Qısa məlumat',
                    ),
                ),
                (
                    'png',
                    models.FileField(
                        help_text='PNG formatda daxil edin. Ölçü: 94x74px',
                        upload_to='services/',
                        verbose_name='PNG',
                    ),
                ),
                (
                    'image',
                    models.ImageField(
                        upload_to='services/images/', verbose_name='Əsas foto'
                    ),
                ),
                (
                    'title',
                    models.CharField(
                        max_length=60,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(30)
                        ],
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_az',
                    models.CharField(
                        max_length=60,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(30)
                        ],
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_en',
                    models.CharField(
                        max_length=60,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(30)
                        ],
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_ru',
                    models.CharField(
                        max_length=60,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(30)
                        ],
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'content',
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name='Servis haqqında geniş məlumat'
                    ),
                ),
                (
                    'content_az',
                    ckeditor_uploader.fields.RichTextUploadingField(
                        null=True, verbose_name='Servis haqqında geniş məlumat'
                    ),
                ),
                (
                    'content_en',
                    ckeditor_uploader.fields.RichTextUploadingField(
                        null=True, verbose_name='Servis haqqında geniş məlumat'
                    ),
                ),
                (
                    'content_ru',
                    ckeditor_uploader.fields.RichTextUploadingField(
                        null=True, verbose_name='Servis haqqında geniş məlumat'
                    ),
                ),
                (
                    'background_color',
                    models.CharField(
                        choices=[
                            ('yellow', 'yellow'),
                            ('green', 'green'),
                            ('blue', 'blue'),
                        ],
                        default='blue',
                        max_length=20,
                    ),
                ),
                (
                    'slug',
                    models.SlugField(
                        blank=True,
                        help_text='Bu qismi boş buraxın. Avtomatik doldurulacaq.',
                        max_length=500,
                        null=True,
                        verbose_name='Link adı',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Xidmət',
                'verbose_name_plural': 'Xidmətlər',
                'ordering': ['-created_at'],
                'indexes': [
                    models.Index(
                        fields=['-created_at'],
                        name='service_ser_created_4b4f5f_idx',
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name='Coworker',
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
                    'name',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 100-dür.',
                        max_length=100,
                        unique=True,
                        verbose_name='Əməkdaş şirkətin adı',
                    ),
                ),
                (
                    'name_az',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 100-dür.',
                        max_length=100,
                        null=True,
                        unique=True,
                        verbose_name='Əməkdaş şirkətin adı',
                    ),
                ),
                (
                    'name_en',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 100-dür.',
                        max_length=100,
                        null=True,
                        unique=True,
                        verbose_name='Əməkdaş şirkətin adı',
                    ),
                ),
                (
                    'name_ru',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 100-dür.',
                        max_length=100,
                        null=True,
                        unique=True,
                        verbose_name='Əməkdaş şirkətin adı',
                    ),
                ),
                (
                    'png',
                    models.FileField(
                        help_text='PNG formatda daxil edin.',
                        upload_to='coworkers/',
                        verbose_name='Logo',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Əməkdaş',
                'verbose_name_plural': 'Əməkdaşlar',
                'ordering': ['-created_at'],
                'indexes': [
                    models.Index(
                        fields=['-created_at'],
                        name='service_cow_created_961b72_idx',
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name='Download',
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
                    'title',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=100,
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_az',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=100,
                        null=True,
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_en',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=100,
                        null=True,
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'title_ru',
                    models.CharField(
                        help_text='Kontentin uzunluğu maksimum 200-dür.',
                        max_length=100,
                        null=True,
                        verbose_name='Başlıq',
                    ),
                ),
                (
                    'type',
                    models.CharField(
                        choices=[('pdf', 'pdf'), ('docx', 'docx')],
                        default='pdf',
                        max_length=4,
                    ),
                ),
                ('file', models.FileField(upload_to='services/downloads')),
                (
                    'service',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='downloads',
                        to='service.service',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Endirmə',
                'verbose_name_plural': 'Endirmələr',
                'ordering': ['-created_at'],
                'indexes': [
                    models.Index(
                        fields=['-created_at'],
                        name='service_dow_created_7792b0_idx',
                    )
                ],
                'unique_together': {('service', 'title')},
            },
        ),
    ]
