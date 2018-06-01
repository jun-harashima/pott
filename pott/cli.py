# -*- coding: utf-8 -*-

import click
import sys
from pott.librarian import Librarian
from pott.utils.input_utils import get_requested_ids, NEXT_INPUTS, QUIT_INPUTS
from pott.utils.output_utils import show_results


@click.group()
def main():
    pass


@main.command()
@click.option('--global', '-g', 'target', flag_value='global', default=True)
@click.option('--local', '-l', 'target', flag_value='local')
@click.argument('keywords', nargs=-1)
@click.option('--year-low', '-yl', 'year_low')
@click.option('--year-high', '-yh', 'year_high')
@click.option('--start', '-s', 'start', default=0)
def search(target, keywords, year_low, year_high, start):
    if target == 'global':
        _global_search(keywords, year_low, year_high, start)
    elif target == 'local':
        _local_search(keywords)


def _global_search(keywords, year_low, year_high, start):
    librarian = Librarian()
    papers = []
    while True:
        _papers = librarian.global_search(keywords, start, year_low, year_high)
        show_results(_papers, start)
        papers.extend(_papers)
        requested_ids, special_input = get_requested_ids(papers)
        if special_input in NEXT_INPUTS:
            start += 10
        elif special_input in QUIT_INPUTS:
            return 0
        else:
            requested_papers = [papers[id] for id in requested_ids]
            librarian.save(requested_papers)
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
