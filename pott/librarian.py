# -*- coding: utf-8 -*-

from pott.index import Index
from pott.yaml import Yaml


class Librarian:

    def __init__(self):
        self.yaml = Yaml()
        self.index = Index()

    def local_search(self, keywords):
        papers = self.index.search(keywords)
        return papers

    def list(self):
        paper_by_id = self.yaml.load()
        return paper_by_id.values()

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
