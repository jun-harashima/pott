# -*- coding: utf-8 -*-

import click
import logging
import requests
import sys
from pott.librarian import Librarian
from pott.utils.input_utils import get_user_input, select


LOG_FILE = 'log.txt'


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
    logger = _set_logger()
    librarian = Librarian()
    papers = librarian.global_search(keywords)
    _show_results(papers)
    user_input = get_user_input(papers)
    selected_papers = select(papers, user_input)
    for paper in selected_papers:
        try:
            librarian.save(paper)
        except requests.ConnectionError as e:
            logger.log(40, str(e))
    return 0


def _local_search(keywords):
    librarian = Librarian()
    papers = librarian.local_search(keywords)
    _show_results(papers)
    return 0


def _set_logger():
    logger = logging.getLogger(__name__)
    fh = logging.FileHandler(LOG_FILE)
    logger.addHandler(fh)
    return logger


def _show_results(papers):
    for index, paper in enumerate(papers):
        print('[' + str(index) + '] ' + paper['title'])
        print('    ' + ', '.join(paper['authors']))


if __name__ == "__main__":
    sys.exit(main())
