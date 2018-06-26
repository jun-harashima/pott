from pott.index import Index
from pott.yaml import Yaml
from pott.screen import Screen


class Assistant:

    PER_PAGE = 10

    def __init__(self):
        self.yaml = Yaml()
        self.index = Index()

    def search(self):
        papers = self._search()
        screen = Screen(self)
        selected_papers = screen.show(papers)
        for paper in selected_papers:
            print(paper.pdf.file_path)

    def search_next(self, papers=[]):
        return self._search_other(self.PER_PAGE)

    def search_previous(self, papers=[]):
        return self._search_other(self.PER_PAGE * -1)

    def _search_other(self, increment):
        original_start = self.option.start
        self.option.start += increment
        papers = self._search()
        if not papers:
            self.option.start = original_start
        return papers

    def is_global(self):
        return self.__class__.__name__ == 'GlobalAssistant'
