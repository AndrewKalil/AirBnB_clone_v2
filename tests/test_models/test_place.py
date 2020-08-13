#!/usr/bin/python3
""" """
import os
import unittest
from models.base_model import BaseModel
from models.place import Place


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "test only for FileStorage")
class TestUser(unittest.TestCase):
    """
        Testing Place class
    """

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.new_place = Place()
        cls.new_place.city_id = "00010"
        cls.new_place.user_id = "1211-asdd-1212-000s"
        cls.new_place.name = "Victoria residence"
        cls.new_place.description = "Comfortable recidence for the families or\
                                     couples looking for a weekend escape"
        cls.new_place.number_rooms = 2
        cls.new_place.number_bathrooms = 2
        cls.new_place.max_guest = 5
        cls.new_place.price_by_night = 60
        cls.new_place.latitude = 42.303993
        cls.new_place.longitude = -123.443211

    def TearDown(self):
        pass

    def test_Place_inheritance(self):
        """
            tests that the City class Inherits from BaseModel
        """

        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        """
            Checks that the attribute exist.
        """
        self.assertTrue("city_id" in self.new_place.__dir__())
        self.assertTrue("user_id" in self.new_place.__dir__())
        self.assertTrue("description" in self.new_place.__dir__())
        self.assertTrue("name" in self.new_place.__dir__())
        self.assertTrue("number_rooms" in self.new_place.__dir__())
        self.assertTrue("max_guest" in self.new_place.__dir__())
        self.assertTrue("price_by_night" in self.new_place.__dir__())
        self.assertTrue("latitude" in self.new_place.__dir__())
        self.assertTrue("longitude" in self.new_place.__dir__())
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

    def test_type_longitude(self):
        """
            Test longitude type
        """
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_latitude(self):
        """
            Test latitude type
        """
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    def test_type_amenity(self):
        """
            Test amenity_ids type
        """
        amenity = getattr(self.new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    def test_type_price_by_night(self):
        """
            Test price_by_night type
        """
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_max_guest(self):
        """
            Test max_guest type
        """
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_number_bathrooms(self):
        """
            Test number_bathrooms type
        """
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_number_rooms(self):
        """
            Test number_bathrooms type
        """
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_description(self):
        """
            Test description type
        """
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    def test_type_name(self):
        """
            Test name type
        """
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    def test_type_user_id(self):
        """
            Test user_id type
        """
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_city_id(self):
        """
            Test city_id type
        """
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)
