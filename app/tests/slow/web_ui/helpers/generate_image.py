import os

from PIL import Image


def generate_invalid_image(filename, size_mb=None):
    with open(f'tests/assets/{filename}', "wb") as f:
        if 'empty' in filename:
            pass
        elif size_mb:
            image = Image.new("RGB", (10, 10), color="red")
            image.save(f, format="PNG")
            f.write(os.urandom(size_mb * 1024 * 1024))  # size_mb in megabytes
        else:
            f.write(b'This is fake file')

    return filename


def generate_valid_image_with_disallowed_extension(filename):

    # Create a simple 10x10 red image
    image = Image.new("RGB", (10, 10), color="red")

    # Save with proper format, but wrong extension
    with open(f'tests/assets/{filename}', "wb") as f:
        image.save(f, format="PNG")  # still writes binary PNG data

    return filename
