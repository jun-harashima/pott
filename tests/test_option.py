import unittest
from pott.option import Option


class TestOption(unittest.TestCase):

    def test___init__(self):
        option = Option(start=0, year_low=None, year_high=None)
        self.assertEqual(option.start, 0)
        self.assertEqual(option.year_low, None)
        self.assertEqual(option.year_high, None)
        self.assertEqual(option.every, None)


if __name__ == "__main__":
    unittest.main()
