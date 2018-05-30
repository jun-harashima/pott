# -*- coding: utf-8 -*-

import click
import requests
import sys
from pott.librarian import Librarian
from pott.utils.input_utils import get_requested_ids
from pott.utils.output_utils import show_results
from pott.utils.log import logger


@click.group()
def main():
    pass


@main.command()
@click.option('--global', '-g', 'target', flag_value='global', default=True)
@click.option('--local', '-l', 'target', flag_value='local')
@click.argument('keywords', nargs=-1)
@click.option('--year-low', '-yl', 'year_low')
@click.option('--year-high', '-yh', 'year_high')
def search(target, keywords, year_low, year_high):
    if target == 'global':
        _global_search(keywords, year_low, year_high)
    elif target == 'local':
        _local_search(keywords)


def _global_search(keywords, year_low, year_high):
    librarian = Librarian()
    papers = librarian.global_search(keywords, year_low, year_high)
    show_results(papers)
    requested_ids = get_requested_ids(papers)
    for paper in [papers[id] for id in requested_ids]:
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
