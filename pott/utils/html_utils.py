import re
from pott.paper import Paper
from pyquery import PyQuery


REGEXP_FOR_AUTHORS = re.compile(r'<a.+?>|</a>|<b>|</b>')
REGEXP_FOR_YEAR = re.compile(r'([0-9]{4}$)')
REGEXP_FOR_CITED_BY = re.compile(r'Cited by ([0-9]+)')


def extract_papers_from(pq_html):
    papers = []
    for div in pq_html.find('div.gs_r.gs_or.gs_scl'):
        pq_div = PyQuery(div)
        paper = _extract_paper_from(pq_div)
        papers.append(paper)
    return papers


def _extract_paper_from(pq_div):
    title = _extract_title_from(pq_div)
    authors, year = _extract_authors_and_year_from(pq_div)
    cited_by = _extract_cited_by_from(pq_div)
    url = _extract_url_from(pq_div)
    snippets = _extract_snippets_from(pq_div)
    return Paper(title, authors, year, cited_by, url, snippets)


def _extract_title_from(pq_div):
    title = pq_div.find('div.gs_ri h3 a').text()
    return title


def _extract_authors_and_year_from(pq_div):
    array = re.split('[  ]- ', pq_div.find('.gs_a').html())
    authors = [re.sub(REGEXP_FOR_AUTHORS, '', author)
               for author in array[0].split(', ')]
    match = re.search(REGEXP_FOR_YEAR, array[1])
    year = match.group(1) if match else None
    return authors, year


def _extract_cited_by_from(pq_div):
    html = pq_div.find('div.gs_ri div.gs_fl').html()
    match = re.search(REGEXP_FOR_CITED_BY, html)
    if not match:
        return ''
    else:
        return match.group(1)


def _extract_url_from(pq_div):
    url = pq_div.find('div.gs_ggs.gs_fl a').attr('href')
    return url


def _extract_snippets_from(pq_div):
    snippets = pq_div.find('div.gs_ri div.gs_rs').html()
    snippets = re.sub(r'<[\w/]+>', '', str(snippets))
    return snippets
