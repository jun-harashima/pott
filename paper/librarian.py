# -*- coding: utf-8 -*-

import re
from pyquery import PyQuery


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar?q="
    __GS_A_REGEXP = re.compile(r'(.+?)(?:&#8230;)? - .+?, (.+?) - .+?')

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
