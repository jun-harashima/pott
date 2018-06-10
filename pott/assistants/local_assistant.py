from pott.assistants.assistant import Assistant


class LocalAssistant(Assistant):

    def _search(self, keywords, options):
        if options.get('every'):
            papers = self.index.search_every()
        else:
            papers = self.index.search(keywords)
        return papers

    def list(self):
        self.search([], {'start': 0, 'every': True})

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
