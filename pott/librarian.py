# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery
from pott.paper_index import PaperIndex
from pott.yaml import Yaml
from pott.files.pdf import Pdf
from pott.files.text import Text
from pott.utils.html_utils import extract_papers_from


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar"

    def __init__(self):
        self.yaml = Yaml()
        self.index = PaperIndex()

    def global_search(self, keywords):
        pq_html = PyQuery(self.__SCHOLAR_URL + '?q=' + ' '.join(keywords))
        papers = extract_papers_from(pq_html)
        return papers

    def save(self, paper):
        print('downloading "' + paper.title + '"')
        response = requests.get(paper.url, timeout=10)
        if response.status_code != 200:
            return
        self._save(paper, response)

    def _save(self, paper, response):
        pdf = Pdf(paper.id + '.pdf')
        pdf.save(response.content)

        text = Text(paper.id + '.txt')
        text.save(pdf.extract_text())

        self.index.save(paper)
        self.yaml.update(paper)

    def local_search(self, keywords):
        papers = self.index.search(keywords)
        return papers

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
