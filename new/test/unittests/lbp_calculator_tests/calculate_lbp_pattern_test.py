import unittest

from lbp_calculate import calculate_lbp_pattern


class CalculateLbpPatternTest(unittest.TestCase):
    brightness_matrix = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 0]
    ]
    valid_pixel_coordinates = (1, 1)
    expected_lbp_pattern_for_pixel_1_1 = [1, 0, 0, 0, 1, 0, 0, 1]

    def test_raises_no_error(self):
        # ACT
        calculate_lbp_pattern(self.brightness_matrix, *self.valid_pixel_coordinates)

        # ASSERT
        self.assertTrue(True)

    def test_pixel_at_y_border_raises_index_error(self):
        try:
            # ACT
            calculate_lbp_pattern(self.brightness_matrix, 1, 0)
            self.assertTrue(False, "No error raised")
        except IndexError:
            self.assertTrue(True)

    def test_return_type_is_list(self):
        # ACT
        lbp_pattern = calculate_lbp_pattern(self.brightness_matrix, *self.valid_pixel_coordinates)

        # ASSERT
        self.assertTrue(type(lbp_pattern) is list)

    def test_list_has_size_8(self):
        # ACT
        lbp_pattern = calculate_lbp_pattern(self.brightness_matrix, *self.valid_pixel_coordinates)

        # ASSERT
        self.assertTrue(len(lbp_pattern) is 8)

    def test_width_and_height_are_correct_calculated(self):
        # ACT
        lbp_pattern = calculate_lbp_pattern(self.brightness_matrix, len(self.brightness_matrix[0]) - 2,
                                            len(self.brightness_matrix) - 2)

        # ASSERT
        self.assertTrue(type(lbp_pattern) is list)

    def test_pattern_matches_expected(self):
        # ACT
        lbp_pattern = calculate_lbp_pattern(self.brightness_matrix, *self.valid_pixel_coordinates)

        # ASSERT
        self.assertEqual(lbp_pattern, self.expected_lbp_pattern_for_pixel_1_1)


if __name__ == "__main__":
    unittest.main()
