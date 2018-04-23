import unittest
from pyquery import PyQuery
from paper.utils.html_utils import extract_papers_from


class TestHtmlUtils(unittest.TestCase):
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
        papers = extract_papers_from(pq_html)
        self.assertEqual(papers, expected_papers)


if __name__ == "__main__":
    unittest.main()
