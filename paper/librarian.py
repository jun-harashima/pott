# -*- coding: utf-8 -*-

import os
import re
import requests
import yaml
from pyquery import PyQuery


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar?q="
    __GS_A_REGEXP = re.compile(r'(.+?)(?:&#8230;)? - .+?, (.+?) - .+?')
    __PDF_DIR = os.environ['HOME'] + '/.paper/pdf'
    __PAPER_YAML = os.environ['HOME'] + '/.paper/paper.yml'

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
        paper['url'] = pq_div.find('div.gs_ggs.gs_fl a').attr('href')
        paper['title'] = pq_div.find('div.gs_ri h3').text()
        match = re.search(self.__GS_A_REGEXP, pq_div.find('.gs_a').html())
        if not match:
            return paper
        for author in match.group(1).split(', '):
            paper['authors'].append(re.sub(r'<a.+?>|</a>', '', author))
        paper['year'] = match.group(2)
        return paper

    def get_user_input(self, papers):
        user_input = input('Paper to download [0-9]: ')
        while not self._is_valid_input(user_input, papers):
            user_input = input('Paper to download [0-9]: ')
        return int(user_input)

    def _is_valid_input(self, user_input, papers):
        if re.match(r'[0-9]', user_input) is None:
            return False
        elif papers[int(user_input)]['url'] is None:
            return False
        else:
            return True

    def save(self, paper):
        response = requests.get(paper['url'])
        if response.status_code != 200:
            return

        if not os.path.isdir(self.__PDF_DIR):
            os.makedirs(self.__PDF_DIR)

        last_name = paper['authors'][0].split(' ')[1]
        file_name = last_name + paper['year'] + '.pdf'
        with open(self.__PDF_DIR + '/' + file_name, 'wb') as pdf_file:
            print('downloading "' + paper['title'] + '"')
            pdf_file.write(response.content)

        self._update_yaml(paper, file_name)

    def _update_yaml(self, paper, file_name):
        if not os.path.isfile(self.__PAPER_YAML):
            with open(self.__PAPER_YAML, 'w') as yaml_file:
                yaml.dump({}, yaml_file, default_flow_style=False)

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
