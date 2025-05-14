import io

from django.core.files.base import ContentFile

from PIL import Image


def generate_png_file(filename="test.png", color="yellow", size=(94, 74)):
    file = io.BytesIO()
    image = Image.new("RGB", size, color=color)
    image.save(file, format="PNG")
    file.seek(0)
    return ContentFile(file.read(), name=filename)
