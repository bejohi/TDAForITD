import unittest

from lba_calculate import calculate_brightness


class CalculateBrightnessTest(unittest.TestCase):
    r_factor = 0.299
    g_factor = 0.587
    b_factor = 0.114

    def test_rbg_111(self):
        # ARRANGE
        r_value = 1
        g_value = 1
        b_value = 1

        # ACT
        brightness = calculate_brightness(r_value, g_value, b_value)

        # ASSERT
        self.assertTrue(brightness == self.r_factor + self.g_factor + self.b_factor)

    def test_rbg_011(self):
        # ARRANGE
        r_value = 0
        g_value = 1
        b_value = 1

        # ACT
        brightness = calculate_brightness(r_value, g_value, b_value)

        # ASSERT
        self.assertTrue(brightness >= self.g_factor + self.b_factor)

    def test_rbg_101(self):
        # ARRANGE
        r_value = 1
        g_value = 0
        b_value = 1

        # ACT
        brightness = calculate_brightness(r_value, g_value, b_value)

        # ASSERT
        self.assertTrue(brightness >= self.r_factor + self.b_factor)

    def test_rbg_110(self):
        # ARRANGE
        r_value = 1
        g_value = 1
        b_value = 0

        # ACT
        brightness = calculate_brightness(r_value, g_value, b_value)

        # ASSERT
        self.assertTrue(brightness >= self.r_factor + self.g_factor)

    def test_rbg_000(self):
        # ARRANGE
        r_value = 0
        g_value = 0
        b_value = 0

        # ACT
        brightness = calculate_brightness(r_value, g_value, b_value)

        # ASSERT
        self.assertTrue(brightness == 0)


if __name__ == "__main__":
    unittest.main()
