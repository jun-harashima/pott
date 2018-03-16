# -*- coding: utf-8 -*-

import click
import sys
from paper.librarian import Librarian


@click.group()
def cmd():
    pass


@cmd.command()
def init():
    librarian = Librarian()
    librarian.initialize()


@cmd.command()
@click.argument('keywords', nargs=-1)
def search(keywords):
    librarian = Librarian()

    if not librarian.is_initialized():
        librarian.initialize()

    papers = librarian.search(keywords)
    for index, paper in enumerate(papers):
        print(str(index) + '. ' + paper['title'], end='')
        print(' (PDF is N/A)' if paper['url'] is None else '')
        print('   ' + ', '.join(paper['authors']))
    user_input = librarian.get_user_input()
    librarian.save(papers[user_input])
    return 0


def main():
    cmd()


if __name__ == "__main__":
    sys.exit(main())
