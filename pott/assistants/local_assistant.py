from pott.assistants.assistant import Assistant


class LocalAssistant(Assistant):

    def _search(self, keywords, options):
        papers = self.index.search(keywords)
        return papers

    def list(self):
        paper_by_id = self.yaml.load()
        return paper_by_id.values()

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
