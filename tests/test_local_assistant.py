import unittest
from unittest.mock import patch
from pott.index import Index
from pott.option import Option
from pott.paper import Paper
from pott.assistants.local_assistant import LocalAssistant


class TestLocalAssistant(unittest.TestCase):

    def test_transform(self):

        option = Option()
        assistant = LocalAssistant(('keyword', ), option)
        self.assertEqual(assistant._transform(option), ())

        option = Option(year_low='2018')
        assistant = LocalAssistant(('keyword', ), option)
        self.assertEqual(assistant._transform(option), ('year:[2018 to]', ))

        option = Option(year_high='2018')
        assistant = LocalAssistant(('keyword', ), option)
        self.assertEqual(assistant._transform(option), ('year:[to 2018]', ))

    def test__search(self):

        paper = Paper()

        with patch.object(Index, 'search_every', return_value=[paper]):
            option = Option(every=True)
            assistant = LocalAssistant((), option)
            self.assertEqual(assistant._search(), [paper])

        with patch.object(Index, 'search', return_value=[paper]):
            option = Option(start=0)
            assistant = LocalAssistant((), option)
            self.assertEqual(assistant._search(), [paper])


if __name__ == "__main__":
    unittest.main()
