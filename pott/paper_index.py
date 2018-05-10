import os
import shutil
from pott.paper import Paper
from whoosh.fields import Schema, ID, TEXT
from whoosh.filedb.filestore import FileStorage
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser


class PaperIndex:

    __TXT_DIR = os.environ['HOME'] + '/.pott/txt'
    __INDEX_DIR = os.environ['HOME'] + '/.pott/index'

    def __init__(self):
        if not os.path.isdir(self.__INDEX_DIR):
            self._create()

    def reindex(self, paper_by_id):
        shutil.rmtree(self.__INDEX_DIR)
        self._create()

        for id, paper in paper_by_id.items():
            self.save(Paper(paper['url'], paper['title']), id, id + '.txt')

    def _create(self):
        os.makedirs(self.__INDEX_DIR)
        schema = Schema(path=ID(unique=True), title=TEXT(stored=True),
                        content=TEXT(stored=True))
        create_in(self.__INDEX_DIR, schema)

    def save(self, paper, paper_prefix, txt_name):
        with open(self.__TXT_DIR + '/' + txt_name, 'r') as txt_file:
            index = open_dir(self.__INDEX_DIR)
            index_writer = index.writer()
            index_writer.add_document(path=paper_prefix, title=paper.title,
                                      content=txt_file.read())
            index_writer.commit()

    def search(self, keywords):
        storage = FileStorage(self.__INDEX_DIR)
        index = storage.open_index()
        query_parser = QueryParser("title", schema=index.schema)
        query = query_parser.parse(' '.join(keywords))
        papers = []
        with index.searcher() as searcher:
            results = searcher.search(query)
            for result in results:
                paper = Paper('', result['title'])
                papers.append(paper)
        return papers
