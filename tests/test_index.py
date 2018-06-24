import shutil
import unittest
from unittest.mock import patch
from pott.index import Index
from pott.paper import Paper

TEST_TXT_DIR = './tests/txt'
TEST_INDEX_DIR = './tests/index'

PAPER1_CONTENT = 'This paper describes my awesome study in 2017'
PAPER2_CONTENT = 'This paper describes my awesome study in 2018'


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.paper1 = Paper('https://smith2017.pdf', 'Awesome Study in 2017',
                            ['John Smith'], '2017')
        self.paper2 = Paper('https://smith2018.pdf', 'Awesome Study in 2018',
                            ['John Smith'], '2018')

    def tearDown(self):
        shutil.rmtree(TEST_INDEX_DIR)

    @patch('pott.index.Index.TXT_DIR', TEST_TXT_DIR)
    @patch('pott.index.Index.INDEX_DIR', TEST_INDEX_DIR)
    def test_search(self):
        Index()._save_content(self.paper1, PAPER1_CONTENT)
        Index()._save_content(self.paper2, PAPER2_CONTENT)

        papers = Index().search(['2017'], 1)
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].title, 'Awesome Study in 2017')
        self.assertEqual(papers[0].authors[0], 'John Smith')
        self.assertEqual(papers[0].year, '2017')

        papers = Index().search(['2018'], 1)
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].title, 'Awesome Study in 2018')
        self.assertEqual(papers[0].authors[0], 'John Smith')
        self.assertEqual(papers[0].year, '2018')

        papers = Index().search(['Awesome'], 1)
        self.assertEqual(len(papers), 2)


if __name__ == "__main__":
    unittest.main()
