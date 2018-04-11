import re

__GS_A_REGEXP = re.compile(r'(.+?)(?:&#8230;)? - .+?, (.+?) - .+?')


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
    return paper
