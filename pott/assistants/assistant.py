from pott.index import Index
from pott.yaml import Yaml
from pott.screen import Screen


class Assistant:

    PER_PAGE = 10

    def __init__(self):
        self.yaml = Yaml()
        self.index = Index()
        self.screen = Screen(self)

    def search(self, keywords, options):
        selected_papers = self.screen.show_papers(keywords, options)
        for paper in selected_papers:
            print(paper.pdf.file_path)

    def _search_next(self, keywords, options, papers=[]):
        return self._search_other(keywords, options, self.PER_PAGE)

    def _search_previous(self, keywords, options, papers=[]):
        return self._search_other(keywords, options, self.PER_PAGE * -1)

    def _search_other(self, keywords, options, increment):
        original_options = options
        options['start'] += increment
        papers = self._search(keywords, options)
        options = original_options if papers else options
        return papers, options

    def _is_GlobalAssistant(self):
        return self.__class__.__name__ == 'GlobalAssistant'
