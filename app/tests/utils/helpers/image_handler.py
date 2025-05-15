import os
from dataclasses import dataclass
from typing import Callable

from tests.utils.helpers import (
    download_image,
    generate_invalid_image,
    generate_valid_image_with_disallowed_extension,
)
from tests.utils.helpers.generate_image import create_empty_image


@dataclass
class ImageHandler:
    """Defines how to generate an image file path for a given image name."""

    condition: Callable[[str], bool]
    generate_path: Callable[[str], str]


class ImageInputHelper:
    def __init__(self):
        self.handlers = [
            ImageHandler(
                condition=lambda name: name == '',
                generate_path=lambda _: download_image(),
            ),
            ImageHandler(
                condition=lambda name: 'invalid' in name,
                generate_path=lambda name: self._generate_asset_path(
                    generate_invalid_image(name)
                ),
            ),
            ImageHandler(
                condition=lambda name: 'disallowed' in name,
                generate_path=lambda name: self._generate_asset_path(
                    generate_valid_image_with_disallowed_extension(name)
                ),
            ),
            ImageHandler(
                condition=lambda name: 'exceed' in name,
                generate_path=lambda name: self._generate_asset_path(
                    generate_invalid_image(name, size_mb=3)
                ),
            ),
            ImageHandler(
                condition=lambda name: 'empty' in name,
                generate_path=lambda name: self._generate_asset_path(
                    create_empty_image(name)
                ),
            ),
        ]

    def _generate_asset_path(self, filename: str) -> str:
        """Generate absolute path for a file in tests/assets."""
        return os.path.abspath(os.path.join("tests/assets", filename))

    def get_image_path(self, image_name):
        for handler in self.handlers:
            if handler.condition(image_name):
                return handler.generate_path(image_name)
        raise ValueError(f"Unsupported image_name: {image_name}")
