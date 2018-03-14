#!/usr/bin/env python


import os
import unittest
from unittest.mock import patch
from paper.librarian import Librarian


class TestInitialize(unittest.TestCase):

    def tearDown(self):
        os.remove('.test_paperconfig')
        os.rmdir('test_dir')

    @patch('builtins.input')
    @patch('paper.librarian.Librarian.CONFIG_FILE', '.test_paperconfig')
    def test_initialize(self, mock_input):
        mock_input.return_value = 'test_dir'
        Librarian().initialize()
        assert os.path.exists('test_dir') == 1
        assert os.path.exists('.test_paperconfig') == 1


    @patch('builtins.input')
    @patch('paper.librarian.Librarian.CONFIG_FILE', '.test_paperconfig')
    def test_is_initialized(self, mock_input):
        mock_input.return_value = 'test_dir'
        Librarian().initialize()
        assert Librarian().is_initialized() == 1


if __name__ == "__main__":
    unittest.main()
