import unittest
from pott.assistants.global_assistant import GlobalAssistant
from pott.assistants.local_assistant import LocalAssistant


class TestAssistant(unittest.TestCase):

    def test_is_global(self):
        self.assertEqual(GlobalAssistant([], {}).is_global(), True)
        self.assertEqual(LocalAssistant([], {}).is_global(), False)


if __name__ == "__main__":
    unittest.main()
