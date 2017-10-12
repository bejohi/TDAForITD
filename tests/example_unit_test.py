import unittest


class ExampleUnitTest(unittest.TestCase):
    def test_example_method(self):
        """Important: Test Methods must start with the keyword ('test')! """
        self.assertEqual("one", "one")


if __name__ == "__main__":
    unittest.main()
