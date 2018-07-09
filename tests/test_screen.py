import unittest
from unittest.mock import patch
from pott.screen import Screen
from pott.paper import Paper
from pott.assistants.assistant import Assistant


class TestScreen(unittest.TestCase):

    @patch.object(Screen, '_move')
    def test__act_on_key_for_key_down(self, mock__move):
        assistant = Assistant()
        screen = Screen(assistant)
        papers = [Paper(), Paper()]
        screen._act_on_key(258, 2, 0, [], papers)  # 258: KEY_DOWN
        mock__move.assert_called_once_with(3)

    @patch.object(Screen, '_move')
    def test__act_on_key_for_key_down_for_edge_case(self, mock__move):
        assistant = Assistant()
        screen = Screen(assistant)
        papers = [Paper(), Paper()]
        screen._act_on_key(258, 3, 0, [], papers)
        mock__move.assert_not_called()

    @patch.object(Screen, '_move')
    def test__act_on_key_for_key_up(self, mock__move):
        assistant = Assistant()
        screen = Screen(assistant)
        screen._act_on_key(259, 3, 0, [], [Paper()])  # 258: KEY_UP
        mock__move.assert_called_once_with(2)


if __name__ == "__main__":
    unittest.main()
