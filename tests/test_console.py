#!/usr/bin/python3
"""Unittest console Module"""
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import unittest
from unittest.mock import patch
import models
import pep8
import os
from io import StringIO
from datetime import datetime


class TestConsole(unittest.TestCase):
    """Test Console Module"""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand testing teardown.
        Restore original file.json.
        Delete the test HBNBCommand instance.
        """
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""

        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_emptyline(self):
        """Test empty line input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_show(self):
        """Test show command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show asdfsdrfs")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show BaseModel abcd-123")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create(self):
        """Test create command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            us = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            st = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            pl = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            ct = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Review")
            rv = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            am = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all User")
            self.assertIn(us, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertIn(st, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            self.assertIn(pl, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all City")
            self.assertIn(ct, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Review")
            self.assertIn(rv, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Amenity")
            self.assertIn(am, f.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create_kwargs(self):
        """Test create command with kwargs."""
        with patch("sys.stdout", new=StringIO()) as f:
            call = ('create Place city_id="0001" name="My_house" '
                    'number_rooms=4 latitude=37.77 longitude=a')
            self.HBNB.onecmd(call)
            pl = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': 'My house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'latitude': 37.77", output)
            self.assertNotIn("'longitude'", output)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "Not using db")
    def test_all(self):
        """Test all command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_destroy(self):
        """Test destroy command input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy Galaxy")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

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
