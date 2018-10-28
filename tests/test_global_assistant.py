import unittest
from unittest.mock import patch
from pott.option import Option
from pott.paper import Paper
from pott.assistants.global_assistant import GlobalAssistant


class TestGlobalAssistant(unittest.TestCase):

    def test_save(self):
        with patch.object(GlobalAssistant, '_download', return_value=None):
            assistant = GlobalAssistant(('keyword', ), Option())
            paper = Paper('Awesome Study in 2018')
            self.assertEqual(assistant.save(paper), False)


if __name__ == "__main__":
    unittest.main()
