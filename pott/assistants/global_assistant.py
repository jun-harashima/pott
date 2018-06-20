import requests
from pyquery import PyQuery
from pott.assistants.assistant import Assistant
from pott.utils.html_utils import extract_papers_from
from pott.utils.log import logger


class GlobalAssistant(Assistant):

    SCHOLAR_URL = "https://scholar.google.com/scholar"

    def __init__(self, keywords, options):
        self.keywords = keywords
        self.options = options
        super().__init__()

    def _search(self):
        url = self._set_url()
        pq_html = PyQuery(url)
        papers = extract_papers_from(pq_html)
        return papers

    def _set_url(self):
        url = self.SCHOLAR_URL + '?q=' + ' '.join(self.keywords)
        if self.options['start'] != 0:
            url += '&start=' + str(self.options['start'])
        if self.options['year_low'] is not None:
            url += '&as_ylo=' + self.options['year_low']
        if self.options['year_high'] is not None:
            url += '&as_yhi=' + self.options['year_high']
        return url

    def search_next(self, papers):
        if self.options['start'] < 990:
            papers = super().search_next()
        return papers

    def search_previous(self, papers):
        if self.options['start'] > 0:
            papers = super().search_previous()
        return papers

    def have_indexed(self, paper):
        return self.yaml.have(paper)

    def save(self, paper):
        response = self._download(paper)
        paper.pdf.save(response.content)
        paper.text.save(paper.pdf.extract_text())
        self.index.save(paper)
        self.yaml.update(paper)

    def _download(self, paper):
        try:
            response = requests.get(paper.url, timeout=10)
            if response.status_code == 200:
                return response
        except requests.ConnectionError as e:
            logger.warn(str(e))
