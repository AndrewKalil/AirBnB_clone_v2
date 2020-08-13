#!/usr/bin/python3
""" test for user module"""
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from io import StringIO
import sys
import datetime


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "test only for FileStorage")
class TestUser(unittest.TestCase):
    """
        Testing User class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.new_user = User()
        cls.new_user.first_name = "Andrew"
        cls.new_user.last_name = "Kalil"
        cls.new_user.email = "andrewlito@gmail.com"
        cls.new_user.password = "quetelocrea..."

    def test_User_inheritance(self):
        """
            tests that the User class Inherits from BaseModel
        """
        self.assertIsInstance(self.new_user, BaseModel)

    def test_User_attributes(self):
        """
            Test the user attributes exist
        """

        self.assertTrue("email" in self.new_user.__dict__)
        self.assertTrue("first_name" in self.new_user.__dict__)
        self.assertTrue("last_name" in self.new_user.__dict__)
        self.assertTrue("id" in self.new_user.__dict__)
        self.assertTrue("password" in self.new_user.__dict__)
        self.assertTrue("created_at" in self.new_user.__dict__)
        self.assertTrue("updated_at" in self.new_user.__dict__)

    def test_type_email(self):
        """
            Test the type of name
        """
        name = getattr(self.new_user, "email")
        self.assertIsInstance(name, str)

    def test_type_first_name(self):
        """
            Test the type of name
        """
        name = getattr(self.new_user, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):
        """
            Test the type of last_name
        """
        name = getattr(self.new_user, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        """
            Test the type of password
        """
        name = getattr(self.new_user, "password")
        self.assertIsInstance(name, str)

    def test_docstring(self):
        """Test documentation"""
        u = User.__doc__
        self.assertGreater(len(u), 1)

if __name__ == '__main__':
    unittest.main()
