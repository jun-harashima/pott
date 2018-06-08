from pott.assistants.assistant import Assistant


class LocalAssistant(Assistant):

    def _get_papers(self, keywords, year_low, year_high, start):
        papers = self.index.search(keywords)
        return papers

    def _get_next_papers(self, keywords, year_low, year_high, start):
        papers = self._get_papers(keywords, year_low, year_high, start + 10)
        start = start if papers else start + 10
        return papers, start

    def _get_previous_papers(self, keywords, year_low, year_high, start):
        papers = self._get_papers(keywords, year_low, year_high, start - 10)
        start = start if papers else start - 10
        return papers, start

    def list(self):
        paper_by_id = self.yaml.load()
        return paper_by_id.values()

    def reindex(self):
        paper_by_id = self.yaml.load()
        self.index.reindex(paper_by_id)
