import unittest
from pott.option import Option
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


if __name__ == "__main__":
    unittest.main()
