import os
import shutil
from pott.paper import Paper
from whoosh.fields import Schema, ID, KEYWORD, TEXT
from whoosh.filedb.filestore import FileStorage
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from whoosh.query import Every


class Index:

    TXT_DIR = os.environ['HOME'] + '/.pott/txt'
    INDEX_DIR = os.environ['HOME'] + '/.pott/index'

    def __init__(self):
        if not os.path.isdir(self.INDEX_DIR):
            self._create()

    def reindex(self, paper_by_id):
        shutil.rmtree(self.INDEX_DIR)
        self._create()

        for paper in paper_by_id.values():
            print('indexing "' + paper.title + '"')
            self.save(paper)

    def _create(self):
        os.makedirs(self.INDEX_DIR)
        schema = Schema(id=ID(unique=True), title=TEXT(stored=True),
                        content=TEXT(stored=True),
                        authors=KEYWORD(stored=True, commas=True),
                        year=ID(stored=True))
        create_in(self.INDEX_DIR, schema)

    def save(self, paper):
        with open(self.TXT_DIR + '/' + paper.id + '.txt', 'r') as txt_file:
            self._save_content(paper, txt_file.read())

    def _save_content(self, paper, content):
        index = open_dir(self.INDEX_DIR)
        index_writer = index.writer()
        index_writer.add_document(id=paper.id, title=paper.title,
                                  content=content,
                                  authors=','.join(paper.authors),
                                  year=paper.year)
        index_writer.commit()

    def search(self, keywords, pagenum):
        storage = FileStorage(self.INDEX_DIR)
        index = storage.open_index()
        query_parser = QueryParser("title", schema=index.schema)
        query = query_parser.parse(' '.join(keywords))
        papers = []
        with index.searcher() as searcher:
            page = searcher.search_page(query, pagenum)
            for result in page:
                paper = Paper('', result['title'],
                              result['authors'].split(','), result['year'])
                papers.append(paper)
        return papers

    def search_every(self):
        storage = FileStorage(self.INDEX_DIR)
        index = storage.open_index()
        query = Every()
        papers = []
        with index.searcher() as searcher:
            results = searcher.search(query, limit=None)
            for result in results:
                paper = Paper('', result['title'],
                              result['authors'].split(','), result['year'])
                papers.append(paper)
        return papers
