import re
from pyquery import PyQuery


__GS_A_REGEXP = re.compile(r'(.+?)(?:&#8230;)? - .+?, (.+?) - .+?')


def extract_papers_from(pq_html):
    papers = []
    for div in pq_html.find('div.gs_r.gs_or.gs_scl'):
        pq_div = PyQuery(div)
        paper = extract_paper_from(pq_div)
        papers.append(paper)
    return papers


def extract_paper_from(pq_div):
    paper = {'url': '', 'title': '', 'authors': [], 'year': 0}
    paper['url'] = pq_div.find('div.gs_ggs.gs_fl a').attr('href')
    paper['title'] = pq_div.find('div.gs_ri h3').text()
    match = re.search(__GS_A_REGEXP, pq_div.find('.gs_a').html())
    if not match:
        return paper
    for author in match.group(1).split(', '):
        paper['authors'].append(re.sub(r'<a.+?>|</a>', '', author))
    paper['year'] = match.group(2)
    paper['id'] = paper['authors'][0].split(' ')[-1] + paper['year']
    return paper
