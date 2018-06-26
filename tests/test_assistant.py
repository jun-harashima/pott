import unittest
from unittest.mock import patch
from pott.option import Option
from pott.paper import Paper
from pott.assistants.global_assistant import GlobalAssistant
from pott.assistants.local_assistant import LocalAssistant


class TestAssistant(unittest.TestCase):

    @patch('pott.assistants.assistant.Assistant._search_other')
    def test_search_previous_for_global_search(self, mock_method):
        current_papers = [Paper('https://smith2018.pdf')]
        previous_papers = [Paper('https://smith2017.pdf')]
        mock_method.return_value = previous_papers

        assistant = GlobalAssistant((), Option(start=10))
        returned_papers = assistant.search_previous(current_papers)
        self.assertEqual(returned_papers, previous_papers)

        assistant = GlobalAssistant((), Option(start=0))
        returned_papers = assistant.search_previous(current_papers)
        self.assertEqual(returned_papers, current_papers)

    @patch('pott.assistants.assistant.Assistant._search_other')
    def test_search_previous_for_local_search(self, mock_method):
        current_papers = [Paper('https://smith2018.pdf')]
        previous_papers = [Paper('https://smith2017.pdf')]
        mock_method.return_value = previous_papers

        assistant = LocalAssistant((), Option(start=10))
        returned_papers = assistant.search_previous(current_papers)
        self.assertEqual(returned_papers, previous_papers)

        assistant = LocalAssistant((), Option(start=0))
        returned_papers = assistant.search_previous(current_papers)
        self.assertEqual(returned_papers, current_papers)

    def test__search_other(self):

        with patch.object(GlobalAssistant, '_search', return_value=[Paper()]):
            assistant = GlobalAssistant((), Option(start=0))
            self.assertEqual(assistant.option.start, 0)
            assistant._search_other(GlobalAssistant.PER_PAGE)
            self.assertEqual(assistant.option.start, GlobalAssistant.PER_PAGE)

        with patch.object(GlobalAssistant, '_search', return_value=[]):
            assistant = GlobalAssistant((), Option(start=0))
            self.assertEqual(assistant.option.start, 0)
            assistant._search_other(GlobalAssistant.PER_PAGE)
            self.assertEqual(assistant.option.start, 0)

    def test__is_global(self):
        self.assertEqual(GlobalAssistant((), Option()).is_global(), True)
        self.assertEqual(LocalAssistant((), Option()).is_global(), False)


if __name__ == "__main__":
    unittest.main()
