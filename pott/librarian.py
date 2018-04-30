# -*- coding: utf-8 -*-

import os
import requests
from pyquery import PyQuery
from pott.utils.html_utils import extract_papers_from
from pott.utils.pdf_utils import extract_text_from
from pott.utils.yaml import Yaml
from pott.utils.paper_index import PaperIndex


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar"
    __PDF_DIR = os.environ['HOME'] + '/.pott/pdf'
    __TXT_DIR = os.environ['HOME'] + '/.pott/txt'

    def __init__(self):
        if not os.path.isdir(self.__PDF_DIR):
            os.makedirs(self.__PDF_DIR)

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

        pdf_name = paper['id'] + '.pdf'
        txt_name = paper['id'] + '.txt'

        with open(self.__PDF_DIR + '/' + pdf_name, 'wb') as pdf_file:
            pdf_file.write(response.content)

        with open(self.__PDF_DIR + '/' + pdf_name, 'rb') as pdf_file:
            text = extract_text_from(pdf_file)
            with open(self.__TXT_DIR + '/' + txt_name, 'w') as txt_file:
                txt_file.write(text)

        self.index.save(paper, paper['id'], txt_name)
        self.yaml.update(paper)

    def local_search(self, keywords):
        papers = self.index.search(keywords)
        return papers
