# -*- coding: utf-8 -*-

import os
import re
import requests
import yaml
from pyquery import PyQuery


class Librarian:

    CONFIG_FILE = '.paperconfig'
    __SCHOLAR_URL = "https://scholar.google.com/scholar?q="
    __GS_A_REGEXP = re.compile(r'(.+?)(?:&#8230;)? - .+?, (.+?) - .+?')

    def initialize(self):
        paper_dir = input('Directory to save papers: ')
        with open(self.CONFIG_FILE, 'w') as f:
            yaml.dump({'paper_dir': paper_dir}, f, default_flow_style=False)
        if not os.path.isdir(paper_dir):
            os.mkdir(paper_dir)

    def is_initialized(self):
        return os.path.isfile(self.CONFIG_FILE)

    def search(self, keywords):
        pq_html = PyQuery(self.__SCHOLAR_URL + ' '.join(keywords))
        papers = self._extract_papers_from(pq_html)
        return papers

    def _extract_papers_from(self, pq_html):
        papers = []
        for div in pq_html.find('div.gs_r.gs_or.gs_scl'):
            pq_div = PyQuery(div)
            paper = self._extract_paper_from(pq_div)
            papers.append(paper)
        return papers

    def _extract_paper_from(self, pq_div):
        paper = {'url': '', 'title': '', 'authors': [], 'year': 0}
        paper['url'] = pq_div.find('h3 a').attr('href')
        paper['title'] = pq_div.find('h3').text()
        match = re.search(self.__GS_A_REGEXP, pq_div.find('.gs_a').html())
        if match:
            for author in match.group(1).split(', '):
                paper['authors'].append(re.sub(r'<a.+?>|</a>', '', author))
            paper['year'] = match.group(2)
        return paper

    def get_user_input(self):
        user_input = input('Paper to download [0-9]: ')
        while re.match(r'[0-9]', user_input) is None:
            user_input = input('Paper to download [0-9]: ')
        return int(user_input)

    def save(self, paper):
        response = requests.get(paper['url'])
        if response.status_code == 200:
            with open(self.__CONFIG_FILE, 'r+') as config_file:
                config = yaml.load(config_file)
            last_name = paper['authors'][0].split(' ')[1]
            file_name = last_name + paper['year'] + '.pdf'
            with open(config['paper_dir'] + '/' + file_name, 'wb') as pdf_file:
                pdf_file.write(response.content)
