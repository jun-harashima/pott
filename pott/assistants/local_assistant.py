from pott.assistants.assistant import Assistant


class LocalAssistant(Assistant):

    def __init__(self, keywords, option):
        _keywords = self._transform(option)
        self.keywords = keywords + _keywords
        self.option = option
        super().__init__()

    def _transform(self, option):
        keywords = []
        if option.year_low:
            keywords.append('year:[{} to]'.format(option.year_low))
        if option.year_high:
            keywords.append('year:[to {}]'.format(option.year_high))
        return tuple(keywords)

    def _search(self):
        if self.option.every:
            papers = self.index.search_every()
        else:
            papers = self.index.search(self.keywords)
        return papers

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
