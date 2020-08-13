#!/usr/bin/python3
""" """
from tests.test_models import test_base_model
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.new_city = City()
        cls.new_city.state_id = "21234"
        cls.new_city.name = "Miami"

    def test_state_id(self):
        """
            check id state_id is string
        """
        self.assertEqual(type(self.new_city.state_id), str)

    def test_name(self):
        """
            check if name is string
        """
        self.assertEqual(type(self.new_city.name), str)

    def test_City_inheritance(self):
        '''
            tests that the City class inherits from BaseModel
        '''
        self.assertIsInstance(self.new_city, BaseModel)

    def test_User_attributes(self):
        """
            Check for attributes
        """
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())
