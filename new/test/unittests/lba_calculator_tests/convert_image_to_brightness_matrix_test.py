import unittest

from lba_calculate import convert_image_to_brightness_matrix
from new.test.unittests.mock_image import Image


class ConvertImageToBrightnessMatrixTest(unittest.TestCase):
    def test_not_raises_index_error(self):
        # ARRANGE
        image = Image(10, 10)

        # ACT AND ASSERT
        convert_image_to_brightness_matrix(image)

    def test_correct_width_and_height(self):
        # ARRANGE
        img_width = 10
        img_height = 5
        image = Image(img_width, img_height)

        # ACT
        matrix = convert_image_to_brightness_matrix(image)

        # ASSERT
        self.assertEqual(len(matrix), img_height)
        self.assertEqual(len(matrix[0]), img_width)


if __name__ == "__main__":
    unittest.main()
