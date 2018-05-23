# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery
from pott.index import Index
from pott.yaml import Yaml
from pott.utils.html_utils import extract_papers_from


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar"

    def __init__(self):
        self.yaml = Yaml()
        self.index = Index()

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
        paper.pdf.save(response.content)
        paper.text.save(paper.pdf.extract_text())
        self.index.save(paper)
        self.yaml.update(paper)

    def local_search(self, keywords):
        papers = self.index.search(keywords)
        return papers

    def list(self):
        paper_by_id = self.yaml.load()
        return paper_by_id.values()

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
