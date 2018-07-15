import unittest
from unittest.mock import patch
from pott.option import Option
from pott.paper import Paper
from pott.yaml import Yaml
from pott.assistants.assistant import Assistant
from pott.assistants.global_assistant import GlobalAssistant
from pott.assistants.local_assistant import LocalAssistant


class TestAssistant(unittest.TestCase):

    @patch('pott.assistants.assistant.Assistant._search_other')
    def test_search_previous_for_global_search(self, mock_method):
        current_papers = [Paper('Awesome Study in 2018')]
        previous_papers = [Paper('Awesome Study in 2017')]
        mock_method.return_value = previous_papers

        assistant = GlobalAssistant((), Option(start=10))
        returned_papers = assistant.search_previous(current_papers)
        self.assertEqual(returned_papers, previous_papers)

        assistant = GlobalAssistant((), Option(start=0))
        returned_papers = assistant.search_previous(current_papers)
        self.assertEqual(returned_papers, current_papers)

    @patch('pott.assistants.assistant.Assistant._search_other')
    def test_search_previous_for_local_search(self, mock_method):
        current_papers = [Paper('Awesome Study in 2018')]
        previous_papers = [Paper('Awesome Study in 2017')]
        mock_method.return_value = previous_papers

        assistant = LocalAssistant((), Option(start=10))
        returned_papers = assistant.search_previous(current_papers)
        self.assertEqual(returned_papers, previous_papers)

        assistant = LocalAssistant((), Option(start=0))
        returned_papers = assistant.search_previous(current_papers)
        self.assertEqual(returned_papers, current_papers)

    def test__search_other(self):

        with patch.object(GlobalAssistant, '_search',
                          return_value=[Paper('Awesome Study in 2018')]):
            assistant = GlobalAssistant((), Option(start=0))
            self.assertEqual(assistant.option.start, 0)
            assistant._search_other(GlobalAssistant.PER_PAGE)
            self.assertEqual(assistant.option.start, GlobalAssistant.PER_PAGE)

        with patch.object(GlobalAssistant, '_search', return_value=[]):
            assistant = GlobalAssistant((), Option(start=0))
            self.assertEqual(assistant.option.start, 0)
            assistant._search_other(GlobalAssistant.PER_PAGE)
            self.assertEqual(assistant.option.start, 0)

    def test_have_indexed(self):
        assistant = Assistant()
        paper = Paper('Awesome Study in 2018')

        with patch.object(Yaml, 'have', return_value=True):
            self.assertEqual(assistant.have_indexed(paper), True)

        with patch.object(Yaml, 'have', return_value=False):
            self.assertEqual(assistant.have_indexed(paper), False)


if __name__ == "__main__":
    unittest.main()
