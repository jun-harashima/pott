#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `paper` package."""


import unittest
from click.testing import CliRunner

from paper import cli


class TestPaper(unittest.TestCase):
    """Tests for `paper` package."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
