import requests
from pyquery import PyQuery
from pott.assistants.assistant import Assistant
from pott.utils.html_utils import extract_papers_from
from pott.utils.log import logger


class GlobalAssistant(Assistant):

    SCHOLAR_URL = "https://scholar.google.com/scholar"

    def __init__(self, keywords, option):
        self.keywords = keywords
        super().__init__(option)

    def _search(self):
        url = self._set_url()
        pq_html = PyQuery(url)
        papers = extract_papers_from(pq_html)
        return papers

    def _set_url(self):
        url = self.SCHOLAR_URL + '?q=' + ' '.join(self.keywords)
        if self.option.start != 0:
            url += '&start=' + str(self.option.start)
        if self.option.year_low is not None:
            url += '&as_ylo=' + self.option.year_low
        if self.option.year_high is not None:
            url += '&as_yhi=' + self.option.year_high
        return url

    def search_next(self, papers):
        if self.option.start < 990:
            papers = super().search_next()
        return papers

    def save(self, paper):
        response = self._download(paper)
        if response is None:
            return False
        text = paper.pdf.extract_text()
        paper.pdf.save(response.content)
        paper.text.save(text)
        self.index.save(paper)
        self.ngram.take_in(text)
        self.yaml.update(paper)
        return True

    def _download(self, paper):
        try:
            response = requests.get(paper.url, timeout=10)
            if response.status_code == 200:
                return response
        except requests.ConnectionError as e:
            logger.warn(str(e))
