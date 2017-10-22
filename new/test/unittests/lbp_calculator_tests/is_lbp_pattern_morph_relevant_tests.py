import unittest

from lbp_calculate import is_lbp_pattern_morph_relevant


class IsLbpPatternMorphRelevantTests(unittest.TestCase):
    def test_empty_list_returns_false(self):
        # ARRANGE
        lbp_pattern = []

        # ACT
        is_relevant = is_lbp_pattern_morph_relevant(lbp_pattern)

        # ASSERT
        self.assertFalse(is_relevant)

    def test_relevant_list_1_returns_true(self):
        # ARRANGE
        lbp_pattern = [1, 1, 0, 0, 0, 0, 0, 0]

        # ACT
        is_relevant = is_lbp_pattern_morph_relevant(lbp_pattern)

        # ASSERT
        self.assertTrue(is_relevant)

    def test_relevant_list_2_returns_true(self):
        # ARRANGE
        lbp_pattern = [1, 0, 0, 0, 0, 0, 0, 1]

        # ACT
        is_relevant = is_lbp_pattern_morph_relevant(lbp_pattern)

        # ASSERT
        self.assertTrue(is_relevant)

    def test_relevant_list_3_returns_true(self):
        # ARRANGE
        lbp_pattern = [0, 0, 0, 1, 1, 0, 0, 0]

        # ACT
        is_relevant = is_lbp_pattern_morph_relevant(lbp_pattern)

        # ASSERT
        self.assertTrue(is_relevant)

    def test_list_with_only_leading_1_returns_false(self):
        # ARRANGE
        lbp_pattern = [1, 0, 0, 0, 0, 0, 0, 0]

        # ACT
        is_relevant = is_lbp_pattern_morph_relevant(lbp_pattern)

        # ASSERT
        self.assertFalse(is_relevant)

    def test_list_with_only_0s_returns_false(self):
        # ARRANGE
        lbp_pattern = [0, 0, 0, 0, 0, 0, 0, 0]

        # ACT
        is_relevant = is_lbp_pattern_morph_relevant(lbp_pattern)

        # ASSERT
        self.assertFalse(is_relevant)

    def test_list_with_2x_1s_but_not_neighbours_returns_false(self):
        # ARRANGE
        lbp_pattern = [1, 0, 0, 0, 0, 0, 1, 0]

        # ACT
        is_relevant = is_lbp_pattern_morph_relevant(lbp_pattern)

        # ASSERT
        self.assertFalse(is_relevant)

    def test_list_with_2x_1s_but_not_neighbours_2_returns_false(self):
        # ARRANGE
        lbp_pattern = [0, 0, 0, 0, 1, 0, 0, 1]

        # ACT
        is_relevant = is_lbp_pattern_morph_relevant(lbp_pattern)

        # ASSERT
        self.assertFalse(is_relevant)


if __name__ == "__main__":
    unittest.main()
