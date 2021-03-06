#!/usr/bin/python3
""" Test for review module """

import os
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.new_review = Review()
        cls.new_review.place_id = "21234"
        cls.new_review.user_id = "1211-asdd-1212-000s"
        cls.new_review.text = "texttexttexttexttexttext"

    def test_Review_inheritance(self):
        """tests that the Review class Inherits from BaseModel"""
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        """Test that Review class has place_id, user_id and text
            attributes."""
        self.assertTrue("place_id" in self.new_review.__dir__())
        self.assertTrue("user_id" in self.new_review.__dir__())
        self.assertTrue("text" in self.new_review.__dir__())
        place_id = getattr(self.new_review, "place_id")
        user_id = getattr(self.new_review, "user_id")
        text = getattr(self.new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == 'fs',
        "This test only work in DBStorage")
    def test_save_Review(self):
        """Test if the Save Working"""
        self.new_review.save()
        self.assertNotEqual(self.new_review.created_at,
                            self.new_review.updated_at)

    def test_to_dict_Review(self):
        """Test if Dictionary working"""
        self.assertEqual('to_dict' in dir(self.new_review), True)

if __name__ == '__main__':
    unittest.main()
