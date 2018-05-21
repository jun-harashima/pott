# -*- coding: utf-8 -*-

import click
import requests
import sys
from pott.librarian import Librarian
from pott.utils.input_utils import get_user_input, select
from pott.utils.output_utils import show_results
from pott.utils.log import logger


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
    papers = librarian.global_search(keywords)
    show_results(papers)
    inputted_ids = get_user_input(papers)
    selected_papers = select(papers, inputted_ids)
    for paper in selected_papers:
        try:
            librarian.save(paper)
        except requests.ConnectionError as e:
            logger.warn(str(e))
    return 0


def _local_search(keywords):
    librarian = Librarian()
    papers = librarian.local_search(keywords)
    show_results(papers)
    return 0


@main.command()
def list():
    librarian = Librarian()
    papers = librarian.list()
    show_results(papers)
    return 0


@main.command()
def reindex():
    librarian = Librarian()
    librarian.reindex()
    return 0


if __name__ == "__main__":
    sys.exit(main())
