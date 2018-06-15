import os
import unittest
import yaml
from unittest.mock import patch
from pott.paper import Paper
from pott.yaml import Yaml

TEST_FILE = 'test.yaml'

PAPER1 = Paper('https://smith2017.pdf', 'Awesome Study in 2017',
               ['John Smith'], '2017')
PAPER2 = Paper('https://smith2018.pdf', 'Awesome Study in 2018',
               ['John Smith'], '2018')


class TestYaml(unittest.TestCase):

    def setUp(self):
        with open(TEST_FILE, 'w') as file:
            dict = {'url': PAPER1.url, 'title': PAPER1.title,
                    'authors': PAPER1.authors, 'year': PAPER1.year}
            papers_by_id = {'Smith2017': dict}
            yaml.dump(papers_by_id, file, default_flow_style=False)

    def tearDown(self):
        os.remove(TEST_FILE)

    @patch('pott.yaml.Yaml.YAML_FILE', TEST_FILE)
    def test_update(self):
        Yaml().update(PAPER2)
        with open(TEST_FILE, 'r') as file:
            papers_by_id = yaml.load(file)
        self.assertEqual(papers_by_id['Smith2017']['url'],
                         'https://smith2017.pdf')
        self.assertEqual(papers_by_id['Smith2018']['url'],
                         'https://smith2018.pdf')

    @patch('pott.yaml.Yaml.YAML_FILE', TEST_FILE)
    def test_have(self):
        self.assertEqual(Yaml().have(PAPER1), True)
        self.assertEqual(Yaml().have(PAPER2), False)


if __name__ == "__main__":
    unittest.main()
