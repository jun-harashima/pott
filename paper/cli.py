# -*- coding: utf-8 -*-

import click
import os
import sys
import yaml
from paper.librarian import Librarian


@click.group()
def cmd():
    pass


@cmd.command()
def init():
    print('Directory to save papers: ', end='')
    paper_dir = input()
    with open('.paperconfig', 'w') as f:
        yaml.dump({'paper_dir': paper_dir}, f, default_flow_style=False)
    if not os.path.isdir(paper_dir):
        os.mkdir(paper_dir)


@cmd.command()
@click.argument('keywords', nargs=-1)
def search(keywords):
    librarian = Librarian()
    papers = librarian.search(keywords)
    for index, paper in enumerate(papers):
        print('- ' + str(index) + '. ' + paper['title'])
    user_input = librarian.get_user_input()
    return 0


def main():
    cmd()


if __name__ == "__main__":
    sys.exit(main())
