import os
import traceback
import unittest

from scripts.image_processing.image_processing import ImageProcessor


class ImageProcessorTest(unittest.TestCase):
    """Tests the ImageProcessor with a real example image."""
    EXAMPLE_IMAGE_PATH = os.path.join("data_storage/images/example_image_davinci.png")
    EXAMPLE_IMAGE_WIDTH = 800
    EXAMPLE_IMAGE_HEIGHT = 800
    EXAMPLE_IMAGE_BRIGHTNESS_IN_POINT_0_0 = 178

    def test_image_load_with_correct_path_should_not_throw_error(self):
        try:
            # ARRANGE
            image_processor = ImageProcessor()

            # ACT
            image_processor.load_image(self.EXAMPLE_IMAGE_PATH)

        except Exception:

            # ASSERT
            self.assertTrue(False, traceback.format_exc())

    def test_image_load_with_wrong_path_should_throw_error(self):
        try:
            # ARRANGE
            image_processor = ImageProcessor()

            # ACT
            image_processor.load_image(" ")

        except FileNotFoundError:
            self.assertTrue(True)

    def test_image_width(self):
        # ARRANGE & ACT
        image_processor = ImageProcessor(self.EXAMPLE_IMAGE_PATH)

        # ASSERT
        self.assertEqual(image_processor.width, self.EXAMPLE_IMAGE_WIDTH)

    def test_image_height(self):
        # ARRANGE & ACT
        image_processor = ImageProcessor(self.EXAMPLE_IMAGE_PATH)

        # ASSERT
        self.assertEqual(image_processor.height, self.EXAMPLE_IMAGE_HEIGHT)

    def test_image_pixels_minimum_throws_no_error(self):
        # ARRANGE & ACT
        image_processor = ImageProcessor(self.EXAMPLE_IMAGE_PATH)

        # ASSERT
        image_processor.pixels[0, 0]  # Should not throw an exception

    def test_image_pixels_maximum_throws_no_error(self):
        # ARRANGE & ACT
        image_processor = ImageProcessor(self.EXAMPLE_IMAGE_PATH)

        # ASSERT
        image_processor.pixels[
            self.EXAMPLE_IMAGE_HEIGHT - 1, self.EXAMPLE_IMAGE_WIDTH - 1]  # Should not throw an exception

    def test_image_brightness(self):
        # ARRANGE
        image_processor = ImageProcessor(self.EXAMPLE_IMAGE_PATH)

        # ACT
        brightness = int(image_processor.get_brightness_of_pixel(0, 0))

        # ASSERT
        self.assertEqual(brightness, self.EXAMPLE_IMAGE_BRIGHTNESS_IN_POINT_0_0)


if __name__ == "__main__":
    unittest.main()
