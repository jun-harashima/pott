#!/usr/bin/env python


import unittest
from paper.librarian import Librarian
from pyquery import PyQuery


class TestLibrarian(unittest.TestCase):
    def test_extract_papers_from(self):
        html = """
        <html>
          <div class="gs_r gs_or gs_scl">
            <div class="gs_ggs gs_fl">
              <a href="paper_url"></a>
            </div>
            <div class="gs_ri">
              <h3>title</h3>
              <div class="gs_a">author - conference, year - site_url</div>
            </div>
          </div>
        </html>
        """

        expected_papers = [
            {
                'url': 'paper_url',
                'title': 'title',
                'authors': ['author'],
                'year': 'year',
            }
        ]

        pq_html = PyQuery(html)
        papers = Librarian()._extract_papers_from(pq_html)
        self.assertEqual(papers, expected_papers)

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
        librarian = Librarian()
        self.assertEqual(librarian._is_valid_input('a', papers), False)
        self.assertEqual(librarian._is_valid_input('0', papers), False)
        self.assertEqual(librarian._is_valid_input('1', papers), True)


if __name__ == "__main__":
    unittest.main()
