from texttable import Texttable

HEADERS = ['ID', 'PDF', 'FIRST AUTHOR', 'YEAR', 'TITLE']


def show_results(papers):
    rows = [HEADERS]
    for index, paper in enumerate(papers):
        first_author = paper.authors[0] if paper.authors else ''
        year = paper.year if paper.year is not None else ''
        title = paper.title
        pdf = '  A' if paper.url is not None else 'N/A'
        row = [index, pdf, first_author, year, title]
        rows.append(row)

    table = Texttable()
    table.set_cols_align(['r', 'r', 'l', 'r', 'l'])
    table.set_cols_width([2, 3, 12, 4, 79])
    table.add_rows(rows)
    print(table.draw())
