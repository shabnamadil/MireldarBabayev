# Generated by Django 4.2.17 on 2025-04-11 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Rəy müəllifi',
            ),
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to='blog.blog',
                verbose_name='Bloq',
            ),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='blogs',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Müəllif',
            ),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(
                related_name='blogs',
                to='blog.category',
                verbose_name='Kateqoriya',
            ),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(
                blank=True,
                related_name='blogs',
                to='blog.tag',
                verbose_name='Teq',
            ),
        ),
        migrations.AddField(
            model_name='blog',
            name='viewed_ips',
            field=models.ManyToManyField(
                editable=False,
                related_name='blogs',
                to='blog.ip',
                verbose_name='Məqalənin görüntüləndiyi IP ünvanları',
            ),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(
                fields=['-created_at'], name='blog_commen_created_1f5393_idx'
            ),
        ),
        migrations.AddIndex(
            model_name='blog',
            index=models.Index(
                fields=['-published_at'], name='blog_blog_publish_fd0506_idx'
            ),
        ),
    ]
