import unittest
from unittest.mock import patch
from pott.option import Option
from pott.paper import Paper
from pott.assistants.global_assistant import GlobalAssistant
from pott.assistants.local_assistant import LocalAssistant


class TestAssistant(unittest.TestCase):

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
