# -*- coding: utf-8 -*-

import os
import requests
import yaml
from pyquery import PyQuery
from paper.utils.html_utils import extract_papers_from
from paper.utils.pdf_utils import extract_text_from
from paper.utils.paper_index import PaperIndex


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar"
    __PDF_DIR = os.environ['HOME'] + '/.paper/pdf'
    __TXT_DIR = os.environ['HOME'] + '/.paper/txt'
    __PAPER_YAML = os.environ['HOME'] + '/.paper/paper.yml'

    def __init__(self):
        if not os.path.isdir(self.__PDF_DIR):
            os.makedirs(self.__PDF_DIR)

        if not os.path.isdir(self.__TXT_DIR):
            os.makedirs(self.__TXT_DIR)

        if not os.path.isfile(self.__PAPER_YAML):
            with open(self.__PAPER_YAML, 'w') as file:
                yaml.dump({}, file, default_flow_style=False)

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

        last_name = paper['authors'][0].split(' ')[1]
        paper_prefix = last_name + paper['year']
        pdf_name = paper_prefix + '.pdf'
        txt_name = paper_prefix + '.txt'

        with open(self.__PDF_DIR + '/' + pdf_name, 'wb') as pdf_file:
            pdf_file.write(response.content)

        with open(self.__PDF_DIR + '/' + pdf_name, 'rb') as pdf_file:
            text = extract_text_from(pdf_file)
            with open(self.__TXT_DIR + '/' + txt_name, 'w') as txt_file:
                txt_file.write(text)

        self.index.save(paper, paper_prefix, txt_name)

        self._update_yaml(paper, pdf_name)

    def _update_yaml(self, paper, file_name):
        with open(self.__PAPER_YAML, 'r') as yaml_file:
            data = yaml.load(yaml_file)

        with open(self.__PAPER_YAML, 'w') as yaml_file:
            data[file_name] = {
                'title':   paper['title'],
                'authors': paper['authors'],
                'year':    paper['year'],
                'url':     paper['url'],
            }
            yaml.dump(data, yaml_file, default_flow_style=False)

    def local_search(self, keywords):
        papers = self.index.search(keywords)
        return papers
