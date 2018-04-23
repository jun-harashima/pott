# -*- coding: utf-8 -*-

import os
import requests
import yaml
from pyquery import PyQuery
from whoosh.fields import Schema, ID, TEXT
from whoosh.index import create_in, open_dir
from whoosh.filedb.filestore import FileStorage
from whoosh.qparser import QueryParser
from paper.utils.html_utils import extract_papers_from
from paper.utils.pdf_utils import extract_text_from


class Librarian:

    __SCHOLAR_URL = "https://scholar.google.com/scholar"
    __PDF_DIR = os.environ['HOME'] + '/.paper/pdf'
    __TXT_DIR = os.environ['HOME'] + '/.paper/txt'
    __INDEX_DIR = os.environ['HOME'] + '/.paper/index'
    __PAPER_YAML = os.environ['HOME'] + '/.paper/paper.yml'

    def __init__(self):
        if not os.path.isdir(self.__PDF_DIR):
            os.makedirs(self.__PDF_DIR)

        if not os.path.isdir(self.__TXT_DIR):
            os.makedirs(self.__TXT_DIR)

        if not os.path.isdir(self.__INDEX_DIR):
            os.makedirs(self.__INDEX_DIR)

        if not os.path.isfile(self.__PAPER_YAML):
            with open(self.__PAPER_YAML, 'w') as file:
                yaml.dump({}, file, default_flow_style=False)

    def global_search(self, keywords):
        pq_html = PyQuery(self.__SCHOLAR_URL + '?q=' + ' '.join(keywords))
        papers = extract_papers_from(pq_html)
        return papers

    def save(self, paper):
        print('downloading "' + paper['title'] + '"')

        response = requests.get(paper['url'], timeout=10)

        if response.status_code != 200:
            return

        last_name = paper['authors'][0].split(' ')[1]
        paper_prefix = last_name + paper['year']
        pdf_name = paper_prefix + '.pdf'
        txt_name = paper_prefix + '.txt'

        with open(self.__PDF_DIR + '/' + pdf_name, 'wb') as pdf_file:
            pdf_file.write(response.content)

        with open(self.__PDF_DIR + '/' + pdf_name, 'rb') as pdf_file:
            text = extract_text_from(pdf_file)
            with open(self.__TXT_DIR + '/' + txt_name, 'w') as txt_file:
                txt_file.write(text)

        with open(self.__TXT_DIR + '/' + txt_name, 'r') as txt_file:
            schema = Schema(path=ID(unique=True), title=TEXT(stored=True),
                            content=TEXT(stored=True))
            create_in(self.__INDEX_DIR, schema)
            index = open_dir(self.__INDEX_DIR)
            index_writer = index.writer()
            index_writer.add_document(path=paper_prefix, title=paper['title'],
                                      content=txt_file.read())
            index_writer.commit()

        self._update_yaml(paper, pdf_name)

    def _update_yaml(self, paper, file_name):
        with open(self.__PAPER_YAML, 'r') as yaml_file:
            data = yaml.load(yaml_file)

        with open(self.__PAPER_YAML, 'w') as yaml_file:
            data[file_name] = {
                'title':   paper['title'],
                'authors': paper['authors'],
                'year':    paper['year'],
                'url':     paper['url'],
            }
            yaml.dump(data, yaml_file, default_flow_style=False)

    def local_search(self, keywords):
        storage = FileStorage(self.__INDEX_DIR)
        index = storage.open_index()
        query_parser = QueryParser("title", schema=index.schema)
        query = query_parser.parse(' '.join(keywords))
        papers = []
        with index.searcher() as searcher:
            results = searcher.search(query)
            for result in results:
                paper = {
                    'url': '',
                    'title': result['title'],
                    'authors': [],
                    'year': 0,
                }
                papers.append(paper)
        return papers
