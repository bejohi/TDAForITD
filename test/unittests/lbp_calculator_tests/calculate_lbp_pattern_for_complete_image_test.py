import unittest

from morphdetect.lbp_calculate import calculate_lbp_pattern_for_complete_image


class CalculateLbpPatternForCompleteImageTests(unittest.TestCase):
    brightness_matrix = [
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 1],
    ]

    def test_raises_no_error(self):
        # ACT
        calculate_lbp_pattern_for_complete_image(self.brightness_matrix)

        # ASSERT
        self.assertTrue(True)

    def test_matrix_size_matches(self):
        # ACT
        lbp_matrix = calculate_lbp_pattern_for_complete_image(self.brightness_matrix)

        # ASSERT
        self.assertTrue(len(lbp_matrix) == len(self.brightness_matrix))
        self.assertTrue(len(lbp_matrix[0]) == len(self.brightness_matrix[0]))

    def test_empty_matrix_returns_empty_matrix(self):
        # ACT
        lbp_matrix = calculate_lbp_pattern_for_complete_image([])

        # ASSERT
        self.assertTrue(len(lbp_matrix) is 0)

    def test_small_matrix_returns_matrix_with_empty_lists(self):
        # ARRANGE
        small_matrix = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        # ACT
        lbp_matrix = calculate_lbp_pattern_for_complete_image(small_matrix)

        # ASSERT
        self.assertTrue(len(lbp_matrix) == 2)
        self.assertTrue(len(lbp_matrix[0]) == 3)
        self.assertTrue(lbp_matrix[0][0] == [])
        self.assertTrue(lbp_matrix[0][1] == [])
        self.assertTrue(lbp_matrix[1][0] == [])
        self.assertTrue(lbp_matrix[1][1] == [])


if __name__ == "__main__":
    unittest.main()
