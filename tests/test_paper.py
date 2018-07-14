import unittest
from pott.paper import Paper


class TestPaper(unittest.TestCase):

    def test___init__(self):
        paper = Paper('Awesome Study in 2017', ['John Smith'], '2017', 10,
                      'https://smith2017.pdf')
        self.assertEqual(paper.title, 'Awesome Study in 2017')
        self.assertEqual(paper.authors, ['John Smith'])
        self.assertEqual(paper.year, '2017')
        self.assertEqual(paper.cited_by, 10)
        self.assertEqual(paper.url, 'https://smith2017.pdf')
        self.assertEqual(paper.id, 'Smith2017')


if __name__ == "__main__":
    unittest.main()
