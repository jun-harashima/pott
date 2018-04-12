import unittest
from paper.utils.input_utils import _is_valid_input


class TestInputUtils(unittest.TestCase):
    def test_is_valid_input(self):
        papers = [
            {
                'url': None,
                'title': 'title1',
                'authors': ['author1'],
                'year': 'year1',
            },
            {
                'url': 'paper_url2',
                'title': 'title2',
                'authors': ['author2'],
                'year': 'year2',
            }
        ]
        self.assertEqual(_is_valid_input('a', papers), False)
        self.assertEqual(_is_valid_input('0', papers), False)
        self.assertEqual(_is_valid_input('1', papers), True)
