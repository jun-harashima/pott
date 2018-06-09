import requests
from pyquery import PyQuery
from pott.assistants.assistant import Assistant
from pott.utils.html_utils import extract_papers_from
from pott.utils.log import logger


class GlobalAssistant(Assistant):

    SCHOLAR_URL = "https://scholar.google.com/scholar"

    def _search(self, keywords, options):
        url = self._set_url(keywords, options)
        pq_html = PyQuery(url)
        papers = extract_papers_from(pq_html)
        return papers

    def _set_url(self, keywords, options):
        url = self.SCHOLAR_URL + '?q=' + ' '.join(keywords)
        if options['start'] != 0:
            url += '&start=' + str(options['start'])
        if options['year_low'] is not None:
            url += '&as_ylo=' + options['year_low']
        if options['year_high'] is not None:
            url += '&as_yhi=' + options['year_high']
        return url

    def _search_next(self, keywords, options):
        papers = []
        if options['start'] < 990:
            papers, options = super()._search_next(keywords, options)
        return papers, options

    def _search_previous(self, keywords, options):
        papers = []
        if options['start'] > 0:
            papers, options = super()._search_previous(keywords, options)
        return papers, options

    def _save(self, stdscr, paper):
        stdscr.addstr(13, 0, 'Downloading "' + paper.title + '"')
        stdscr.move(14, 0)
        stdscr.deleteln()
        stdscr.refresh()
        response = self._download(paper)
        paper.pdf.save(response.content)
        paper.text.save(paper.pdf.extract_text())
        self.index.save(paper)
        self.yaml.update(paper)
        stdscr.addstr(14, 0, 'Saved as "' + paper.pdf.file_path + '"')

    def _download(self, paper):
        try:
            response = requests.get(paper.url, timeout=10)
            if response.status_code == 200:
                return response
        except requests.ConnectionError as e:
            logger.warn(str(e))
