from pott.index import Index
from pott.yaml import Yaml
from pott.screen import Screen


class Assistant:

    PER_PAGE = 10

    def __init__(self, keywords, options):
        self.keywords = keywords
        self.options = options
        self.yaml = Yaml()
        self.index = Index()
        self.screen = Screen(self)

    def search(self):
        selected_papers = self.screen.show_papers()
        for paper in selected_papers:
            print(paper.pdf.file_path)

    def _search_next(self, papers=[]):
        return self._search_other(self.PER_PAGE)

    def _search_previous(self, papers=[]):
        return self._search_other(self.PER_PAGE * -1)

    def _search_other(self, increment):
        original_options = self.options
        self.options['start'] += increment
        papers = self._search()
        self.options = original_options if papers else self.options
        return papers

    def is_global(self):
        return self.__class__.__name__ == 'GlobalAssistant'
