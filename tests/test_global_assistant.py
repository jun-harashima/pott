import unittest
from pott.option import Option
from pott.assistants.global_assistant import GlobalAssistant


class TestGlobalAssistant(unittest.TestCase):

    def test__set_url(self):
        url = GlobalAssistant.SCHOLAR_URL

        assistant = GlobalAssistant(('keyword', ), Option())
        self.assertEqual(assistant._set_url(), url + '?q=keyword')

        assistant = GlobalAssistant(('keyword', ), Option(start=10))
        self.assertEqual(assistant._set_url(), url + '?q=keyword&start=10')

        assistant = GlobalAssistant(('keyword', ), Option(year_low='2018'))
        self.assertEqual(assistant._set_url(), url + '?q=keyword&as_ylo=2018')

        assistant = GlobalAssistant(('keyword', ), Option(year_high='2018'))
        self.assertEqual(assistant._set_url(), url + '?q=keyword&as_yhi=2018')


if __name__ == "__main__":
    unittest.main()
