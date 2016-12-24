#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_turbo_sqlalchemy
----------------------------------

Tests for `turbo_sqlalchemy` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from turbo_sqlalchemy import turbo_sqlalchemy
from turbo_sqlalchemy import cli



class TestTurbo_sqlalchemy(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'turbo_sqlalchemy.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output