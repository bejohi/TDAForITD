import os

from scripts.image_handling.image_information import ImageInfo
from scripts.image_handling.pixel_processor import PixelProcessor


class TestBase:
    EXAMPLE_IMAGE_PATH = os.path.join("data_storage/images/example_image_davinci.png")
    EXAMPLE_IMAGE_WIDTH = 800
    EXAMPLE_IMAGE_HEIGHT = 800
    EXAMPLE_IMAGE_BRIGHTNESS_IN_POINT_0_0 = 178
    image_info = ImageInfo(EXAMPLE_IMAGE_PATH)
    pixel_processor = PixelProcessor(image_info)
