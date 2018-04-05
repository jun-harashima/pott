# -*- coding: utf-8 -*-

import os
import re
import requests
import yaml
from pyquery import PyQuery
from utils.html_utils import extract_paper_from
from utils.pdf_utils import extract_text_from


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar?q="
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

    def search(self, keywords):
        pq_html = PyQuery(self.__SCHOLAR_URL + ' '.join(keywords))
        papers = self._extract_papers_from(pq_html)
        return papers

    def _extract_papers_from(self, pq_html):
        papers = []
        for div in pq_html.find('div.gs_r.gs_or.gs_scl'):
            pq_div = PyQuery(div)
            paper = extract_paper_from(pq_div)
            papers.append(paper)
        return papers

    def get_user_input(self, papers):
        user_input = input('Paper to download [0-9] or all: ')
        while not self._is_valid_input(user_input, papers):
            user_input = input('Paper to download [0-9] or all: ')
        return user_input

    def _is_valid_input(self, user_input, papers):
        if user_input == 'all':
            return True
        elif re.match(r'[0-9]', user_input) is None:
            return False
        elif papers[int(user_input)]['url'] is None:
            return False
        elif papers[int(user_input)]['authors'] == []:
            return False
        else:
            return True

    def select(self, papers, user_input):
        if user_input == 'all':
            return [paper for paper in papers
                    if not paper['url'] is None and not paper['authors'] == []]
        else:
            return [papers[int(user_input)]]

    def save(self, paper):
        print('downloading "' + paper['title'] + '"')

        response = requests.get(paper['url'], timeout=10)

        if response.status_code != 200:
            return

        last_name = paper['authors'][0].split(' ')[1]
        pdf_name = last_name + paper['year'] + '.pdf'
        txt_name = last_name + paper['year'] + '.txt'

        with open(self.__PDF_DIR + '/' + pdf_name, 'wb') as pdf_file:
            pdf_file.write(response.content)

        with open(self.__PDF_DIR + '/' + pdf_name, 'rb') as pdf_file:
            text = extract_text_from(pdf_file)
            with open(self.__TXT_DIR + '/' + txt_name, 'w') as txt_file:
                txt_file.write(text)

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
