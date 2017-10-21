import unittest

from lba_calculate import convert_image_to_brightness_matrix
from new.test.unittests.mock_image import Image


class ConvertImageToBrightnessMatrixTest(unittest.TestCase):
    def test_not_raises_index_error(self):
        # ARRANGE
        image = Image(10)

        # ACT AND ASSERT
        convert_image_to_brightness_matrix(image)


if __name__ == "__main__":
    unittest.main()
