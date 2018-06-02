from texttable import Texttable

HEADERS = ['ID', 'PDF', 'FIRST AUTHOR', 'YEAR', 'CITED BY', 'TITLE']


def show_results(papers, start=0):
    rows = [HEADERS]
    for index, paper in enumerate(papers):
        first_author = paper.authors[0] if paper.authors else ''
        year = paper.year if paper.year is not None else ''
        title = paper.title
        pdf = '  A' if paper.url is not None else 'N/A'
        cited_by = paper.cited_by if paper.cited_by is not None else ''
        row = [index + start, pdf, first_author, year, cited_by, title]
        rows.append(row)

    table = Texttable()
    table.set_cols_align(['r', 'r', 'l', 'r', 'r', 'l'])
    table.set_cols_width([2, 3, 12, 4, 8, 79])
    table.add_rows(rows)
    print(table.draw())
