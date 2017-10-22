import unittest

from morphdetect.lbp_calculate import convert_image_to_brightness_matrix
from test.unittests.mock_image import Image


class ConvertImageToBrightnessMatrixTest(unittest.TestCase):
    def test_not_raises_index_error(self):
        # ARRANGE
        image = Image(10, 10)

        # ACT
        convert_image_to_brightness_matrix(image)

        # ASSERT
        self.assertTrue(True)

    def test_returns_correct_type(self):
        # ARRANGE
        image = Image(10, 10)

        # ACT
        matrix = convert_image_to_brightness_matrix(image)

        # ASSERT
        self.assertTrue(type(matrix[0][0]) is float)

    def test_empty_image_returns_empty_matrix(self):
        # ARRANGE
        image = Image(0, 0)

        # ACT
        matrix = convert_image_to_brightness_matrix(image)

        # ASSERT
        self.assertTrue(len(matrix) == 0)

    def test_empty_x_image_returns_empty_matrix(self):
        # ARRANGE
        image = Image(5, 0)

        # ACT
        matrix = convert_image_to_brightness_matrix(image)

        # ASSERT
        self.assertTrue(len(matrix) == 0)

    def test_correct_width_and_height_with_asymmetric_matrix(self):
        # ARRANGE
        img_width = 10
        img_height = 5
        image = Image(img_width, img_height)

        # ACT
        matrix = convert_image_to_brightness_matrix(image)

        # ASSERT
        self.assertEqual(len(matrix), img_height)
        self.assertEqual(len(matrix[0]), img_width)

    def test_matrix_filled_with_concrete_value(self):
        # ARRANGE
        img_width = 10
        img_height = 5
        image = Image(img_width, img_height)
        image.pixel_matrix[3][5] = (5, 5, 5)
        image.pixel_matrix[1][1] = (1, 1, 1)

        # ACT
        matrix = convert_image_to_brightness_matrix(image)

        # ASSERT
        self.assertTrue(matrix[3][5] > matrix[1][1])


if __name__ == "__main__":
    unittest.main()
