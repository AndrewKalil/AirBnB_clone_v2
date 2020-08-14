#!/usr/bin/python3
""" Test Module for state"""
import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Test the State class."""

    @classmethod
    def setUpClass(cls):
        """set up class"""
        cls.state = State()
        cls.state.name = 'California'

    def test_State_inheritence(self):
        """ Test that State class inherits from BaseModel."""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """Test that State class contains the attribute `name`. """
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == 'fs',
        "This test only work in DBStorage")
    def test_save_state(self):
        """Test if the Save Working"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Test if Dictionary working"""
        self.assertEqual('to_dict' in dir(self.state), True)

if __name__ == '__main__':
    unittest.main()
