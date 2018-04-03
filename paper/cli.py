# -*- coding: utf-8 -*-

import click
import requests
import sys
from paper.librarian import Librarian


@click.group()
def main():
    pass


@main.command()
@click.option('--global', '-g', 'target', flag_value='global', default=True)
@click.option('--local', '-l', 'target', flag_value='local')
@click.argument('keywords', nargs=-1)
def search(target, keywords):
    if target == 'global':
        _global_search(keywords)
    elif target == 'local':
        _local_search(keywords)


def _global_search(keywords):
    librarian = Librarian()
    papers = librarian.search(keywords)
    for index, paper in enumerate(papers):
        print(str(index) + '. ' + paper['title'])
        print(' (PDF is N/A)' if paper['url'] is None else '')
        print('   ' + ', '.join(paper['authors']))
    user_input = librarian.get_user_input(papers)
    selected_papers = librarian.select(papers, user_input)
    for paper in selected_papers:
        try:
            librarian.save(paper)
        except requests.ConnectionError as e:
            print(str(e))
    return 0


def _local_search(keywords):
    return 0


if __name__ == "__main__":
    sys.exit(main())
