import unittest
from pott.utils.input_utils import get_requested_ids
from pott.paper import Paper


class TestInputUtils(unittest.TestCase):

    def test_get_requested_ids(self):
        paper1 = Paper('https://smith2016.pdf', 'Awesome Study in 2016',
                       ['John Smith'], '2016')
        paper2 = Paper('https://smith2017.pdf', 'Awesome Study in 2017',
                       ['John Smith'], '2017')
        paper3 = Paper(None, 'Awesome Study in 2018',
                       ['John Smith'], '2018')
        papers = [paper1, paper2, paper3]

        # Basic usage
        with unittest.mock.patch('builtins.input', side_effect=['0']):
            self.assertEqual(get_requested_ids(papers), [0])

        # Multiple download
        with unittest.mock.patch('builtins.input', side_effect=['0,1']):
            self.assertEqual(get_requested_ids(papers), [0, 1])

        # Ignore unavailable papers
        with unittest.mock.patch('builtins.input', side_effect=['2', '0']):
            self.assertEqual(get_requested_ids(papers), [0])

        # Ignore unavailable papers
        with unittest.mock.patch('builtins.input', side_effect=['0,2', '0']):
            self.assertEqual(get_requested_ids(papers), [0])

        # Ignore invalid IDs
        with unittest.mock.patch('builtins.input', side_effect=['a', '0']):
            self.assertEqual(get_requested_ids(papers), [0])

        # Ignore invalid IDs
        with unittest.mock.patch('builtins.input', side_effect=['0,a', '0']):
            self.assertEqual(get_requested_ids(papers), [0])
