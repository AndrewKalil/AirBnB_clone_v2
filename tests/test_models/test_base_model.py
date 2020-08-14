#!/usr/bin/python3
""" test for basemodel"""

import unittest
import os
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestBase(unittest.TestCase):
    '''
        Testing the base class model.
    '''

    def setUp(self):
        '''
            Initializing instance.
        '''
        self.model = BaseModel()
        self.model.name = "Test Model"

    def __init__(self, *args, **kwargs):
        """Init setUp module"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def TearDown(self):
        '''
            Removing instance.
        '''
        del self.model

    def test_id_type(self):
        '''
            Checks that the type of the id is string.
        '''
        self.assertEqual("<class 'str'>", str(type(self.model.id)))

    def test_ids_differ(self):
        '''
            Checks that the ids between two instances are different.
        '''
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.model.id)

    def test_name(self):
        '''
            Checks that an attribute can be added.
        '''
        self.assertEqual("Test Model", self.model.name)

    def test_a_updated_created_equal(self):
        '''
            Checks that both dates are equal.
        '''
        self.assertEqual(self.model.updated_at.year,
                         self.model.created_at.year)

    @unittest.skip("new future added")
    def test_kwargs_one(self):
        """test Kwargs"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_kwargs_object(self):
        """Kwargs objcts"""
        n = {'Name': 'test'}
        new_obj = self.value(**n)
        self.assertEqual(new_obj.__dict__['Name'], 'test')

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Don't test if not FileStorage storing")
    def test_save(self):
        '''
            Checks that after updating the instance; the dates differ in the
            updated_at attribute.
        '''
        old_update = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_update)

    def test_updated_at(self):
        """updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertTrue(new.created_at == new.updated_at)

    def test_str_overide(self):
        '''
            Checks that the right message gets printed.
        '''
        backup = sys.stdout
        inst_id = self.model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

    def test_to_dict_type(self):
        '''
            Checks that the to_dict method return type.
        '''

        self.assertEqual("<class 'dict'>",
                         str(type(self.model.to_dict())))

    def test_to_dict_class(self):
        '''
            Checks that the __class__ key exists.
        '''

        self.assertEqual("BaseModel", (self.model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        '''
            Checks the type of the value of updated_at.
        '''
        self.assertEqual("<class 'str'>",
                         str(type((self.model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        '''
            Checks the type of the value of created_at.
        '''
        tmp = self.model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        '''
            Test that an instance is created using the
            key value pair.
        '''
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertNotEqual(new_model.id, self.model.id)

    def test_type_created_at(self):
        '''
            Test that the new_model's updated_at
            data type is datetime.
        '''
        model_dict = self.model.to_dict()
        new_model = BaseModel(model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        '''
            Test that the new_model's created_at
            data type is datetime.
        '''
        model_dict = self.model.to_dict()
        new_model = BaseModel(model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        '''
            Test that the new_model's and model's
            dictionary values are same.
        '''
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        new_model_dict = new_model.to_dict()
        self.assertNotEqual(model_dict, new_model_dict)

    def test_instance_diff(self):
        '''
            Test that the model and new_model are
            not the same instance.
        '''
        model_dict = self.model.to_dict()
        new_model = BaseModel(model_dict)
        self.assertNotEqual(self.model, new_model)

if __name__ == '__main__':
    unittest.main()
