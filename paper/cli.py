# -*- coding: utf-8 -*-

import click
import sys
from paper.librarian import Librarian


@click.group()
def main():
    pass


@main.command()
@click.argument('keywords', nargs=-1)
def search(keywords):
    librarian = Librarian()
    papers = librarian.search(keywords)
    for index, paper in enumerate(papers):
        print(str(index) + '. ' + paper['title'])
        print(' (PDF is N/A)' if paper['url'] is None else '')
        print('   ' + ', '.join(paper['authors']))
    user_input = librarian.get_user_input(papers)
    librarian.save(papers[user_input])
    return 0


if __name__ == "__main__":
    sys.exit(main())
