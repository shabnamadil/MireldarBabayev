import os
from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile

from PIL import Image


def generate_invalid_image(filename, size_mb=None):
    with open(f"tests/assets/{filename}", "wb") as f:
        if size_mb:
            image = Image.new("RGB", (10, 10), color="red")
            image.save(f, format="PNG")
            f.write(os.urandom(size_mb * 1024 * 1024))  # size_mb in megabytes
        else:
            f.write(b"This is fake file")

    return filename


def create_empty_image(filename):
    full_path = os.path.abspath(f"tests/assets/{filename}")
    with open(full_path, "wb"):
        pass  # Creates an empty file
    return full_path


def generate_valid_image_with_disallowed_extension(filename):

    # Create a simple 10x10 red image
    image = Image.new("RGB", (10, 10), color="red")

    # Save with proper format, but wrong extension
    with open(f"tests/assets/{filename}", "wb") as f:
        image.save(f, format="PNG")  # still writes binary PNG data

    return filename


def create_valid_test_image():
    buffer = BytesIO()
    image = Image.new("RGB", (100, 100), color="blue")
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    return SimpleUploadedFile("avatar.jpg", buffer.read(), content_type="image/jpeg")
