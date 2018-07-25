import unittest
from unittest.mock import patch
from click.testing import CliRunner
from pott import cli
from pott.yaml import Yaml


class TestCli(unittest.TestCase):

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    @patch.object(Yaml, 'load', return_value={})
    def test_reindex(self, mocked_load):
        runner = CliRunner()
        result = runner.invoke(cli.main, ['reindex'])
        assert result.exit_code == 0


if __name__ == "__main__":
    unittest.main()
