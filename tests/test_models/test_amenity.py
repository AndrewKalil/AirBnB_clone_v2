#!/usr/bin/python3
""" Amenity test module"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel


class test_Amenity(test_basemodel):
    """ test class for amenity"""

    def __init__(self, *args, **kwargs):
        """ Instantiation """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
            test if name is a string
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_Amenity_inheritance(self):
        """
            tests that the Amenity class Inherits from BaseModel
        """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """
            Test that Amenity class had name attribute.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """
            Test that Amenity class had name attribute's type.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)
