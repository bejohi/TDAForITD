import traceback
import unittest

from image_handling import ImageInfo
from obsolete.tests.test_base import TestBase


class ImageInfoTest(unittest.TestCase, TestBase):
    """Tests the ImageProcessor with a real example image."""

    def test_image_load_with_correct_path_should_not_throw_error(self):
        try:
            # ARRANGE
            image_processor = ImageInfo()

            # ACT
            image_processor.load_image(self.EXAMPLE_IMAGE_PATH)

        except Exception:

            # ASSERT
            self.assertTrue(False, traceback.format_exc())

    def test_image_load_with_wrong_path_should_throw_error(self):
        try:
            # ARRANGE
            image_processor = ImageInfo()

            # ACT
            image_processor.load_image(" ")

        except FileNotFoundError:
            self.assertTrue(True)

    def test_image_width(self):
        # ASSERT
        self.assertEqual(self.image_info.width, self.EXAMPLE_IMAGE_WIDTH)

    def test_image_height(self):
        # ASSERT
        self.assertEqual(self.image_info.height, self.EXAMPLE_IMAGE_HEIGHT)

    def test_image_pixels_minimum_throws_no_error(self):
        # ASSERT
        self.image_info.pixels[0, 0]  # Should not throw an exception

    def test_image_pixels_maximum_throws_no_error(self):
        # ASSERT
        self.image_info.pixels[
            self.EXAMPLE_IMAGE_HEIGHT - 1, self.EXAMPLE_IMAGE_WIDTH - 1]  # Should not throw an exception

    def test_image_brightness(self):
        # ACT
        brightness = int(self.image_info.get_brightness_of_pixel(0, 0))

        # ASSERT
        self.assertEqual(brightness, self.EXAMPLE_IMAGE_BRIGHTNESS_IN_POINT_0_0)


if __name__ == "__main__":
    unittest.main()
