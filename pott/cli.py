# -*- coding: utf-8 -*-

import click
import sys
from pott.assistants.global_assistant import GlobalAssistant
from pott.assistants.local_assistant import LocalAssistant
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
    assistant = LocalAssistant() if target == 'local' else GlobalAssistant()
    assistant.search(keywords, year_low, year_high, start)
    return 0


@main.command()
def list():
    assistant = LocalAssistant()
    papers = assistant.list()
    show_results(papers)
    return 0


@main.command()
def reindex():
    assistant = LocalAssistant()
    assistant.reindex()
    return 0


if __name__ == "__main__":
    sys.exit(main())
