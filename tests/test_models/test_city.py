#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """
            instantiation
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
            check id state_id is string
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
            check if name is string
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_City_inheritance(self):
        '''
            tests that the City class inherits from BaseModel
        '''
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        """
            Check for attributes
        """
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())
