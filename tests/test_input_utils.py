import unittest
from pott.paper import Paper
from pott.utils.input_utils import _is_valid_input


class TestInputUtils(unittest.TestCase):
    def test_is_valid_input(self):
        paper1 = Paper(None, '', ['John Smith'])
        paper2 = Paper('https://smith2018.pdf', '', ['John Smith'])
        papers = [paper1, paper2]
        self.assertEqual(_is_valid_input('a', papers), False)
        self.assertEqual(_is_valid_input('0', papers), False)
        self.assertEqual(_is_valid_input('1', papers), True)
