#!/usr/bin/python3
""" Amenity test module"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest
import os


class TestAmenity(unittest.TestCase):
    """ test class for amenity"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.new_amenity = Amenity()
        cls.new_amenity.name = "Wifi"

    def test_name2(self):
        """test if name is a string"""
        self.assertEqual(type(self.new_amenity.name), str)

    def test_Amenity_inheritance(self):
        """tests that the Amenity class Inherits from BaseModel"""
        self.assertIsInstance(self.new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """Test that Amenity class had name attribute."""
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """Test that Amenity class had name attribute's type."""
        name_value = getattr(self.new_amenity, "name")
        self.assertIsInstance(name_value, str)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == 'fs',
        "This test only work in DBStorage")
    def test_save_Amenity(self):
        """Test if the Save Working"""
        self.new_amenity.save()
        self.assertNotEqual(self.new_amenity.created_at,
                            self.new_amenity.updated_at)

    def test_to_dict_Amenity(self):
        """Test if Dictionary working"""
        self.assertEqual('to_dict' in dir(self.new_amenity), True)

if __name__ == '__main__':
    unittest.main()
