import tempfile

from django.conf import settings

import requests


def download_image():
    # Lorem Picsum API URL for a random image
    image_url = "https://picsum.photos/200/300"

    # Download the image content
    response = requests.get(image_url, timeout=settings.DEFAULT_REQUEST_TIMEOUT)

    try:
        if response.status_code == 200:
            # Create a temporary file to store the image
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            with open(temp_file.name, "wb") as f:
                f.write(response.content)
            return temp_file.name
    except Exception as e:
        raise ValueError(f"Failed to download image from Lorem Picsum API:{e}")
