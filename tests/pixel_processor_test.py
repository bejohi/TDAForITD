import unittest

from tests.test_base import TestBase


class PixelProcessorTest(unittest.TestCase, TestBase):
    """Tests the PixelProcessor with real image data."""
    LBP_PATTERN_POINT_1_1 = [1, 1, 1, 1, 1, 1, 1, 1]

    def test_lbp_pattern_matches_with_expected_pattern(self):
        # ACT
        lbp_pattern = self.pixel_processor.calculate_local_binary_pattern(1, 1)

        # ASSERT
        self.assertEqual(lbp_pattern, self.LBP_PATTERN_POINT_1_1)

    def test_lbp_pattern_y_at_border_throes_error(self):
        try:
            self.pixel_processor.calculate_local_binary_pattern(10, 0)
            self.assertTrue(False, "No IndexError thrown")
        except IndexError:
            pass

    def test_lbp_pattern_x_at_border_throes_error(self):
        try:
            self.pixel_processor.calculate_local_binary_pattern(0, 10)
            self.assertTrue(False, "No IndexError thrown")
        except IndexError:
            pass

    def test_lbp_pattern_xy_at_border_throes_error(self):
        try:
            self.pixel_processor.calculate_local_binary_pattern(self.image_info.width-1, self.image_info.height-1)
            self.assertTrue(False, "No IndexError thrown")
        except IndexError:
            pass


if __name__ == "__main__":
    unittest.main()
