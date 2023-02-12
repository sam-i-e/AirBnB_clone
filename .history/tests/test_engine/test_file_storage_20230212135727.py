#!/usr/bin/python3
'''Test file for FileStorage Class
'''
import unittest
import json
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):
    '''TestFileStorage class built to test regular
    and edge case usage of FileStorage Class.
    Inherits from TestCase class in unittest module.
    '''

    def test_file_path_is_private_from_instance(self):
        '''Test to ensure `__file_path` class attribute is a
        private class attribute thus inaccessible when
        referenced through instances
        '''
        with self.assertRaises(AttributeError):
            file_path = storage.__file_path

    def test_file_path_is_private_from_class(self):
        '''Test to ensure `__file_path` private class attribute is a
        private class attribute thus inaccessible when
        referenced through the class.
        '''
        with self.assertRaises(AttributeError):
            file_path = FileStorage.__file_path

    def test_file_path_type(self):
        '''Test fails if `__file_path` private class attribute is not of type
        str
        '''
        self.assertIs(type(FileStorage._FileStorage__file_path), str)

    def test_objects_type(self):
        '''Test fails if `__objects` private class attribute is not of type
        dict
        '''
        self.assertIs(type(FileStorage._FileStorage__objects), dict)

#    def test_all(self):
#        '''Test ensures public instance method `all`
#        returns private class attribute `__objects`
#        '''
#        self.assertEqual(
#            {key: storage.all()[key].to_dict() for key in
#             storage.all().keys()},
#            storage._FileStorage__objects
#        )

    def test_all_return_type(self):
        '''Test ensure the dictionary returned by `all()` public
        instance method has values of type/subtype BaseModel.
        '''
        for value in storage.all().values():
            self.assertIsInstance(value, BaseModel)

    def test_new(self):
        '''Tests to ensure that public instance method `new(obj)`
        intended to add obj to the private class attribute `__objects`
        executes accordingly.
        '''
        prev_count = len(storage.all())
        test_model_0 = BaseModel(
            id=str(uuid.uuid4()),
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        )
        storage.new(test_model_0)
        self.assertEqual(len(storage.all()), prev_count + 1)

    def test_new_accurate(self):
        '''Tests to ensure that public instance method `new(obj)`
        intended to add obj to the private class attribute `__objects`
        stores the obj data accurately.
        '''
        test_model_0 = BaseModel(
            id=str(uuid.uuid4()),
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        )
        storage.new(test_model_0)
        self.assertEqual(
            storage.all()[
                f"{test_model_0.__class__.__name__}.{test_model_0.id}"
            ].to_dict(),
            test_model_0.to_dict()
        )

    def test_objects_key_format(self):
        '''Test the format of all items in the dict stored as
        `__objects` private class attribute to ensure all keys follow format:
        "<class name>.id"
        '''
        test_model_1 = BaseModel()
        test_model_2 = BaseModel()
        objs = storage.all()
        for key in storage.all().keys():
            self.assertEqual(
                key,
                f"{objs[key].__class__.__name__}.{objs[key].id}"
            )

    def test_objects_value_type(self):
        '''Test ensures all items in `__objects` private class
        attribute dictionary have values of type dict.
        '''
        test_model_3 = BaseModel()
        test_model_4 = BaseModel()
        for value in storage._FileStorage__objects.values():
            self.assertIsInstance(value, dict)

    def test_save(self):
        '''Tests the FileStorage public instance method `save()`
        intended to save the current value of private class
        attribute `__objects` to the file specified by `__file_path`
        '''
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
            self.assertIsInstance(data, dict)
            self.assertEqual(data, storage._FileStorage__objects)

    def test_reload(self):
        '''Tests the public instance method `reload` which deserializes
        the JSON in __file_path and assigns it to __objects
        '''
        prev_objs = storage._FileStorage__objects.copy()
        storage.save()
        test_model_5 = BaseModel(
            id=str(uuid.uuid4()),
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        )
        storage.new(test_model_5)
        curr_objs = storage._FileStorage__objects.copy()
        storage.reload()
        self.assertNotEqual(len(prev_objs), len(curr_objs))
        self.assertNotEqual(storage._FileStorage__objects, curr_objs)
        self.assertEqual(storage._FileStorage__objects, prev_objs)


if __name__ == "__main__":
    unittest.main()
