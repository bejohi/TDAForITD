import os
import traceback
import unittest

from scripts.image_processing.image_processing import ImageProcessor


class ImageProcessorTest(unittest.TestCase):
    """Tests the ImageProcessor with a real example image."""
    example_image_path = os.path.join("data_storage/images/example_image_davinci.png")
    EXAMPLE_IMAGE_WIDTH = 800
    EXAMPLE_IMAGE_HEIGHT = 800

    def test_picture_load_with_correct_path_should_not_throw_error(self):
        try:
            # ARRANGE
            image_processor = ImageProcessor()

            # ACT
            image_processor.load_image(self.example_image_path)

        except Exception:

            # ASSERT
            self.assertTrue(False, traceback.format_exc())

    def test_picture_load_with_wrong_path_should_throw_error(self):
        try:
            # ARRANGE
            image_processor = ImageProcessor()

            # ACT
            image_processor.load_image(" ")

        except FileNotFoundError:
            self.assertTrue(True)

    def test_picture_width(self):
        # ARRANGE & ACT
        image_processor = ImageProcessor(self.example_image_path)

        # ASSERT
        self.assertEqual(image_processor.width, self.EXAMPLE_IMAGE_WIDTH)

    def test_picture_height(self):
        # ARRANGE & ACT
        image_processor = ImageProcessor(self.example_image_path)

        # ASSERT
        self.assertEqual(image_processor.height, self.EXAMPLE_IMAGE_HEIGHT)


if __name__ == "__main__":
    unittest.main()
