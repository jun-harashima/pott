# -*- coding: utf-8 -*-

import click
import sys
from pott.assistants.global_assistant import GlobalAssistant
from pott.librarian import Librarian
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
        assitant = GlobalAssistant()
        assitant.search(keywords, year_low, year_high, start)
        return 0
    elif target == 'local':
        _local_search(keywords)


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
