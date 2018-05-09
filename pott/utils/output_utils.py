def show_results(papers):
    print('ID | PDF | FIRST AUTHOR | YEAR | TITLE')
    print('-' * 130)
    for index, paper in enumerate(papers):
        first_author = paper.authors[0] if paper.authors else ''
        year = paper.year if paper.year is not None else ''
        title = paper.title
        pdf = '  A' if paper.url is not None else 'N/A'
        print(' {0} | {1: <2} | {2: <12} | {3: <4} | {4: <20}'
              .format(index, pdf, first_author, year, title))
