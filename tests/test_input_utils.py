import unittest
from pott.utils.input_utils import _is_valid


class TestInputUtils(unittest.TestCase):
    def test_is_valid_input(self):
        self.assertEqual(_is_valid('a'), False)
        self.assertEqual(_is_valid('0'), True)
        self.assertEqual(_is_valid('0,1'), True)
