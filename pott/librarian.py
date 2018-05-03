# -*- coding: utf-8 -*-

import os
import requests
from pyquery import PyQuery
from pott.utils.html_utils import extract_papers_from
from pott.utils.pdf import Pdf
from pott.utils.yaml import Yaml
from pott.utils.paper_index import PaperIndex


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar"
    __TXT_DIR = os.environ['HOME'] + '/.pott/txt'

    def __init__(self):
        if not os.path.isdir(self.__TXT_DIR):
            os.makedirs(self.__TXT_DIR)

        self.yaml = Yaml()
        self.index = PaperIndex()

    def global_search(self, keywords):
        pq_html = PyQuery(self.__SCHOLAR_URL + '?q=' + ' '.join(keywords))
        papers = extract_papers_from(pq_html)
        return papers

    def save(self, paper):
        print('downloading "' + paper['title'] + '"')

        response = requests.get(paper['url'], timeout=10)

        if response.status_code != 200:
            return

        txt_name = paper['id'] + '.txt'

        pdf = Pdf(paper['id'] + '.pdf')
        pdf.save(response.content)
        text = pdf.extract_text()
        with open(self.__TXT_DIR + '/' + txt_name, 'w') as txt_file:
            txt_file.write(text)

        self.index.save(paper, paper['id'], txt_name)
        self.yaml.update(paper)

    def local_search(self, keywords):
        papers = self.index.search(keywords)
        return papers
