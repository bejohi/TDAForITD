import unittest

from scripts.image_handling.image_matrix import ImageMatrix


class ImageMatrixTest(unittest.TestCase):
    def test_height_not_int_raises_type_error(self):
        # ARRANGE
        image_matrix = None
        width = 10
        height = 1.5
        try:
            # ACT & ASSERT
            image_matrix = ImageMatrix(width, height)
            self.assertTrue(False, "No TypeError raised")
        except TypeError:
            self.assertIsNone(image_matrix)

    def test_width_not_int_raises_type_error(self):
        # ARRANGE
        image_matrix = None
        width = 1.5
        height = 10
        try:
            # ACT & ASSERT
            image_matrix = ImageMatrix(width, height)
            self.assertTrue(False, "No TypeError raised")
        except TypeError:
            self.assertIsNone(image_matrix)

    def test_width_negative_raises_value_error(self):
        # ARRANGE
        image_matrix = None
        width = -1
        height = 10
        try:
            # ACT & ASSERT
            image_matrix = ImageMatrix(width, height)
            self.assertTrue(False, "No ValueError raised")
        except ValueError:
            self.assertIsNone(image_matrix)

    def test_height_negative_raises_value_error(self):
        # ARRANGE
        image_matrix = None
        width = 10
        height = -1
        try:
            # ACT & ASSERT
            image_matrix = ImageMatrix(width, height)
            self.assertTrue(False, "No ValueError raised")
        except ValueError:
            self.assertIsNone(image_matrix)

    def test_height_and_width_matrix_ok(self):
        # ARRANGE
        width = 10
        height = 9

        # ACT
        image_matrix = ImageMatrix(width, height)

        # ASSERT
        self.assertIsNotNone(image_matrix)
        self.assertEqual(width, image_matrix.width)
        self.assertEqual(height, image_matrix.height)

    def test_brightness_matrix_correct_initialized(self):
        # ARRANGE
        width = 10
        height = 5

        # ACT
        image_matrix = ImageMatrix(width, height)

        # ASSERT
        self.assertIsNone(image_matrix.brightness_matrix[0][0])
        self.assertIsNone(image_matrix.brightness_matrix[width - 1][height - 1])
        self.assertIsNone(image_matrix.brightness_matrix[0][height - 1])
        self.assertIsNone(image_matrix.brightness_matrix[width - 1][0])

    def test_add_brightness_value_correct_inserted(self):
        # ARRANGE
        width = 10
        height = 10
        brightness = 100
        image_matrix = ImageMatrix(width, height)

        # ACT
        image_matrix.brightness_matrix[width - 1][height - 1] = brightness

        # ASSERT
        self.assertEqual(image_matrix.brightness_matrix[width - 1][height - 1], brightness)


if __name__ == "__main__":
    unittest.main()
