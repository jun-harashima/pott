import os
import unittest
import yaml
from unittest.mock import patch
from pott.utils.yaml import Yaml

TEST_FILE = 'test.yaml'

PAPER1 = {
    'id':  'Smith2017',
    'url': 'https://smith2017.pdf',
    'title': 'Awesome Study in 2017',
    'authors': ['John Smith'],
    'year': '2017',
}

PAPER2 = {
    'id':  'Smith2018',
    'url': 'https://smith2018.pdf',
    'title': 'Awesome Study in 2018',
    'authors': ['John Smith'],
    'year': '2018',
}


class TestYaml(unittest.TestCase):

    def setUp(self):
        with open(TEST_FILE, 'w') as file:
            papers_by_id = {'Smith2017': PAPER1}
            yaml.dump(papers_by_id, file, default_flow_style=False)

    def tearDown(self):
        os.remove(TEST_FILE)

    @patch('pott.utils.yaml.Yaml.YAML_FILE', TEST_FILE)
    def test_update(self):
        Yaml().update(PAPER2)
        with open(TEST_FILE, 'r') as file:
            papers_by_id = yaml.load(file)
        self.assertEqual(papers_by_id,
                         {'Smith2017': PAPER1, 'Smith2018': PAPER2})


if __name__ == "__main__":
    unittest.main()
