#!/usr/bin/python3
"""Unittest console Module"""

import unittest
import os
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from io import StringIO
from datetime import datetime


class TestConsole(unittest.TestCase):
    """Test Console Module"""

    def setUpClass(cls):
        """HBNBCommand testing setup"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""

        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstings(self):
        """Docstring of Each Function"""

        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'preloop'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'precmd'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'postcmd'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'do_quit'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'help_quit'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'do_EOF'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'help_EOF'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'emptyline'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'do_create'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'help_create'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'do_show'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'help_show'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'do_destroy'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'help_destroy'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'do_all'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'help_all'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'do_count'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'help_count'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'do_update'))
        self.assertTrue(HBNBCommand.__init__.__doc__)
        self.assertTrue(hasattr(HBNBCommand, 'help_update'))


if __name__ == '__main__':
    unittest.main()
