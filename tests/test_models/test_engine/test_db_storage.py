#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage
import os
import pep8


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'fs',
        "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @classmethod
    def setUpClass(self):
        """setUpClass module"""
        storage._DBStorage__session.close()
        self.store = DBStorage()
        self.store.reload()

    @classmethod
    def tearDownClass(self):
        """tearDownClass module"""
        self.store._DBStorage__session.close()
        storage.reload()

    def test_all(self):
        """print alls objects"""
        self.assertEqual(len(self.store.all()), 0)
        new_obj = State()
        new_obj.name = 'California'
        self.store.new(new_obj)
        self.assertEqual(len(self.store.all()), 1)
        # Make all('classname') work without console

    def test_new(self):
        """New objects"""
        new_obj = State()
        new_obj.name = "Texas"
        new_obj.save()
        self.assertTrue(len(self.store.all()), 1)

    def test_save(self):
        """save objects"""
        self.store.reload()
        new_obj = State()
        new_obj.name = 'Washington'
        self.store.new(new_obj)
        self.store.save()
        self.assertEqual(len(self.store.all()), 4)

    def test_delete(self):
        new_obj = State()
        new_obj.name = "Michigan"
        self.store.new(new_obj)
        self.store.save()
        self.store.delete(new_obj)
        self.assertFalse(new_obj in self.store.all())

    def test_reload(self):
        """reload datas objects"""
        new_obj = City()
        self.store.new(new_obj)
        self.store.reload()
        test_len = len(self.store.all())
        self.assertEqual(test_len, 3)
        self.store.reload()
        for value in self.store.all().values():
            self.assertIsInstance(value.created_at, datetime)

if __name__ == '__main__':
    unittest.main()
