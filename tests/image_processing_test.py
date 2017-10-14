import os
import traceback
import unittest

from scripts.image_processing.image_processing import ImageProcessor


class ImageProcessorTest(unittest.TestCase):
    example_image_path = os.path.join("data_storage/images/example_image_davinci.png")

    def test_picture_load(self):
        try:
            # ARRANGE
            image_processor = ImageProcessor()

            # ACT
            image_processor.load_image(self.example_image_path)

        except Exception:

            # ASSERT
            self.assertTrue(False, traceback.format_exc())


if __name__ == "__main__":
    unittest.main()
