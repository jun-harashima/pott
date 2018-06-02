import re
from pott.paper import Paper
from pyquery import PyQuery


__GS_A_REGEXP = re.compile(r'(.+?)(?:&#8230;)? - .+?, ([0-9]+?) - .+?')
__GS_FL_REGEXP = re.compile(r'Cited by ([0-9]+)')


def extract_papers_from(pq_html):
    papers = []
    for div in pq_html.find('div.gs_r.gs_or.gs_scl'):
        pq_div = PyQuery(div)
        paper = extract_paper_from(pq_div)
        papers.append(paper)
    return papers


def extract_paper_from(pq_div):
    url = pq_div.find('div.gs_ggs.gs_fl a').attr('href')
    title = pq_div.find('div.gs_ri h3 a').text()
    match = re.search(__GS_A_REGEXP, pq_div.find('.gs_a').html())
    if not match:
        return Paper(url, title)
    authors = []
    for author in match.group(1).split(', '):
        authors.append(re.sub(r'<a.+?>|</a>|<b>|</b>', '', author))
    year = match.group(2)
    cited_by = _extract_cited_by_from(pq_div)
    return Paper(url, title, authors, year, cited_by)


def _extract_cited_by_from(pq_div):
    html = pq_div.find('div.gs_ri div.gs_fl').html()
    match = re.search(__GS_FL_REGEXP, html)
    if not match:
        return ''
    else:
        return match.group(1)
