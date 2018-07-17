import unittest
from unittest.mock import patch
from pott.index import Index
from pott.option import Option
from pott.paper import Paper
from pott.screen import Screen
from pott.assistants.assistant import Assistant
from pott.assistants.local_assistant import LocalAssistant


class TestScreen(unittest.TestCase):

    PAPER1 = Paper('Awesome Study in 2017', ['John Smith'], '2017', 50,
                   'https://smith2017.pdf')
    PAPER2 = Paper('Awesome Study in 2018', ['John Smith'], '2018', 10,
                   'https://smith2018.pdf')

    @patch.object(Screen, '_move')
    def test__act_on_key_for_key_down(self, mock__move):
        assistant = Assistant()
        screen = Screen(assistant)
        papers = [self.PAPER1, self.PAPER2]
        screen._act_on_key(258, 2, 0, [], papers)  # 258: KEY_DOWN
        mock__move.assert_called_once_with(3)

    @patch.object(Screen, '_move')
    def test__act_on_key_for_key_down_for_edge_case(self, mock__move):
        assistant = Assistant()
        screen = Screen(assistant)
        papers = [self.PAPER1, self.PAPER2]
        screen._act_on_key(258, 3, 0, [], papers)
        mock__move.assert_not_called()

    @patch.object(Screen, '_move')
    def test__act_on_key_for_key_up(self, mock__move):
        assistant = Assistant()
        screen = Screen(assistant)
        papers = [self.PAPER1]
        screen._act_on_key(259, 3, 0, [], papers)  # 258: KEY_UP
        mock__move.assert_called_once_with(2)

    @patch.object(Screen, '_update_table')
    @patch.object(Index, 'search', return_value=[PAPER2])
    def test__act_on_key_for_next(self, mock_search, mock__update_table):
        assistant = LocalAssistant((), Option())
        screen = Screen(assistant)
        papers = [self.PAPER1]
        screen._act_on_key(110, 2, 0, [], papers)  # 110: ord('n')
        mock__update_table.assert_called_once_with([self.PAPER2])

    @patch.object(Screen, '_update_table')
    @patch.object(Index, 'search', return_value=[])
    def test__act_on_key_for_next_for_edge_case(self, mock_search,
                                                mock__update_table):
        assistant = LocalAssistant((), Option())
        screen = Screen(assistant)
        papers = [self.PAPER1]
        screen._act_on_key(110, 2, 0, [], papers)
        mock__update_table.assert_not_called()

    def test__act_on_key_for_quit(self):
        assistant = Assistant()
        screen = Screen(assistant)
        papers = [self.PAPER1]
        actual = screen._act_on_key(113, 2, 0, [], papers)  # 113: ord('q')
        desired = (True, [])
        self.assertEqual(actual, desired)


if __name__ == "__main__":
    unittest.main()
