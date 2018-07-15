import unittest
from unittest.mock import patch
from pott.option import Option
from pott.paper import Paper
from pott.assistants.global_assistant import GlobalAssistant


class TestGlobalAssistant(unittest.TestCase):

    def test__set_url(self):
        url = GlobalAssistant.SCHOLAR_URL

        assistant = GlobalAssistant(('keyword', ), Option())
        self.assertEqual(assistant._set_url(), url + '?q=keyword')

        # Do not attach start=0
        assistant = GlobalAssistant(('keyword', ), Option(start=0))
        self.assertEqual(assistant._set_url(), url + '?q=keyword')

        assistant = GlobalAssistant(('keyword', ), Option(start=10))
        self.assertEqual(assistant._set_url(), url + '?q=keyword&start=10')

        assistant = GlobalAssistant(('keyword', ), Option(year_low='2018'))
        self.assertEqual(assistant._set_url(), url + '?q=keyword&as_ylo=2018')

        assistant = GlobalAssistant(('keyword', ), Option(year_high='2018'))
        self.assertEqual(assistant._set_url(), url + '?q=keyword&as_yhi=2018')

    def test_save(self):
        with patch.object(GlobalAssistant, '_download', return_value=None):
            assistant = GlobalAssistant(('keyword', ), Option())
            paper = Paper('Awesome Study in 2018')
            self.assertEqual(assistant.save(paper), False)


if __name__ == "__main__":
    unittest.main()
