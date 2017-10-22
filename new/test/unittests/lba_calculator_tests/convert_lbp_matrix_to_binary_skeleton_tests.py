import unittest

from lbp_calculate import convert_lbp_matrix_to_binary_skeleton


class ConvertLbpMatrixToBinarySkeletonTests(unittest.TestCase):
    lbp_matrix = [
        [[], [], [], [], [], []],
        [[], [1, 1], [1, 0], [0, 0], [0, 1], []],
        [[], [1, 1], [1, 0], [1, 1], [0, 0], []],
        [[], [], [], [], [], []]
    ]
    example_position_of_1 = (1, 1)
    example_position_of_0 = (1, 2)

    def test_returns_list(self):
        # ACT
        binary_skeleton = convert_lbp_matrix_to_binary_skeleton(self.lbp_matrix)

        # ASSERT
        self.assertTrue(type(binary_skeleton) is list)

    def test_size_and_height_are_correct(self):
        # ACT
        binary_skeleton = convert_lbp_matrix_to_binary_skeleton(self.lbp_matrix)

        # ASSERT
        self.assertTrue(len(binary_skeleton) == len(self.lbp_matrix))
        self.assertTrue(len(binary_skeleton[0]) == len(self.lbp_matrix[0]))

    def test_contains_only_1s_and_0s(self):
        # ACT
        binary_skeleton = convert_lbp_matrix_to_binary_skeleton(self.lbp_matrix)

        # ASSERT
        for row in binary_skeleton:
            for binary_value in row:
                if binary_value != 1 and binary_value != 0:
                    self.assertTrue(False, "The skeleton contain other values than 1 or 0.")

    def test_skeleton_has_expected_value(self):
        # ARRANGE
        y_1, x_1 = self.example_position_of_1
        y_0, x_0 = self.example_position_of_0

        # ACT
        binary_skeleton = convert_lbp_matrix_to_binary_skeleton(self.lbp_matrix)

        # ASSERT
        self.assertTrue(binary_skeleton[y_1][x_1] == 1)
        self.assertTrue(binary_skeleton[y_0][x_0] == 0)


if __name__ == "__main__":
    unittest.main()
