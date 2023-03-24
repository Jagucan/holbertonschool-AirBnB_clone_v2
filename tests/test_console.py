#!/usr/bin/python3
""" Test for Console """
import io
import sys
import json
import unittest
from console import HBNBCommand
from unittest.mock import create_autospec


class TestHBNBCommand(unittest.TestCase):
    """ Test for Class HBNBCommand """

    def setUp(self):
        """ Metode for the test """
        self.console = HBNBCommand()

    def test_do_quit(self):
        """ Test to quit """
        self.assertTrue(self.console.onecmd("quit"))

    def test_do_EOF(self):
        """ Test to EOF """
        with self.assertRaises(SystemExit):
            self.console.do_EOF("")

    def create(self, server=None):
        """ Test to saving """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)


if __name__ == '__main__':
    unittest.main()
