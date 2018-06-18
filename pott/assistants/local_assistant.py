from pott.assistants.assistant import Assistant


class LocalAssistant(Assistant):

    def _search(self):
        if self.options.get('every'):
            papers = self.index.search_every()
        else:
            papers = self.index.search(self.keywords)
        return papers

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
