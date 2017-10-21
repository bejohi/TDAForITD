import unittest

from image_handling import Picture
from image_handling import Pixel


class PictureUnitTest(unittest.TestCase):
    example_pixel = Pixel(100, 10, 10)
    example_picture = Picture(100, 100)

    def test_pixel_add_pixel_and_find_by_index_in_matrix(self):
        # ARRANGE
        self.example_picture.add_pixel(self.example_pixel)

        # ACT
        pixel = self.example_picture.pixel_matrix[self.example_pixel.x][self.example_pixel.y]

        # ASSERT
        self.assertEqual(pixel, self.example_pixel)

    def test_pixel_out_of_range_raises_index_error(self):
        # ARRANGE
        pixel_out_of_range = Pixel(100, self.example_picture.width + 1, self.example_picture.height + 1)
        # ACT & ASSERT
        try:
            self.example_picture.add_pixel(pixel_out_of_range)
            self.assertTrue(False, "No IndexError raised")
        except IndexError:
            self.assertTrue(True)

    def test_pixel_negative_index_raises_index_error(self):
        # ARRANGE
        pixel_negative_index = Pixel(100, 1, 1)
        pixel_negative_index.x = -1
        pixel_negative_index.y = -1

        # ACT & ASSERT
        try:
            self.example_picture.add_pixel(pixel_negative_index)
            self.assertTrue(False, "No IndexError raised")
        except IndexError:
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
