from pott.assistants.assistant import Assistant


class LocalAssistant(Assistant):

    def __init__(self, keywords, options):
        _keywords = self._transform(options)
        self.keywords = keywords + _keywords
        self.options = options
        super().__init__()

    def _transform(self, options):
        keywords = []
        if options.get('year_low'):
            keywords.append('year:[{} to]'.format(options['year_low']))
        if options.get('year_high'):
            keywords.append('year:[to {}]'.format(options['year_high']))
        return tuple(keywords)

    def _search(self):
        if self.options.get('every'):
            papers = self.index.search_every()
        else:
            papers = self.index.search(self.keywords)
        return papers

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
