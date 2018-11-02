import requests
from gsch.agent import Agent
from pott.assistants.assistant import Assistant
from pott.log import logger


class GlobalAssistant(Assistant):

    SCHOLAR_URL = "https://scholar.google.com/scholar"

    def __init__(self, keywords, option):
        self.keywords = keywords
        super().__init__(option)

    def _search(self):
        agent = Agent()
        papers = agent.search(self.keywords, self.option)
        return papers

    def search_next(self, papers):
        if self.option.start < 990:
            papers = super().search_next()
        return papers

    def save(self, paper):
        response = self._download(paper)
        if response is None:
            return False
        text = paper.pdf.extract_text()
        paper.pdf.save(response.content)
        paper.text.save(text)
        self.index.save(paper)
        self.ngram.take_in(text)
        self.yaml.update(paper)
        return True

    def _download(self, paper):
        try:
            response = requests.get(paper.url, timeout=10)
            if response.status_code == 200:
                return response
        except requests.ConnectionError as e:
            logger.warn(str(e))
