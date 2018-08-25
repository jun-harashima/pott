from pott.assistants.assistant import Assistant
from pott.screens.kwic_screen import KwicScreen


class LocalAssistant(Assistant):

    def __init__(self, keywords, option):
        _keywords = self._transform(option)
        self.keywords = keywords + _keywords
        super().__init__(option)

    def _transform(self, option):
        keywords = []
        if option.year_low:
            keywords.append('year:[{} to]'.format(option.year_low))
        if option.year_high:
            keywords.append('year:[to {}]'.format(option.year_high))
        return tuple(keywords)

    def _search(self):
        if self.option.every:
            return self.index.search_every()
        pagenum = self.option.start // self.PER_PAGE + 1
        return self.index.search(self.keywords, pagenum)

    def reload(self):
        paper_by_id = self.yaml.load()
        self.index.reload(paper_by_id)
        self.ngram.reload(paper_by_id)

    def kwic(self):
        screen = KwicScreen()
        screen.show()
