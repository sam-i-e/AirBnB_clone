#!/usr/bin/python3
"""Test file for FileStorage Class
"""
import json
import unittest
import uuid
from datetime import datetime

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):
    """TestFileStorage class built to test regular
    and edge case usage of FileStorage Class.
    Inherits from TestCase class in unittest module.
    """

    def setUp(self):
        self.temp_file = "/temp_store.json"
        self.temp_objs = [BaseModel(), BaseModel(), BaseModel()]
        for obj in self.temp_objs:
            storage.new(obj)
        storage.save()

    def tearDown(self):
        """initialized object"""
        del self.temp_objs

    def test_file_path_is_private_from_instance(self):
        """Test to ensure `__file_path` class attribute is a
        private class attribute thus inaccessible when
        referenced through instances
        """
        with self.assertRaises(AttributeError):
            file_path = storage.__file_path

    def test_file_path_is_private_from_class(self):
        """Test to ensure `__file_path` private class attribute is a
        private class attribute thus inaccessible when
        referenced through the class.
        """
        with self.assertRaises(AttributeError):
            file_path = FileStorage.__file_path

    def test_file_path_type(self):
        """Test fails if `__file_path` private class attribute is not of type
        str
        """
        self.assertIs(type(FileStorage._FileStorage__file_path), str)

    def test_objects_type(self):
        """Test fails if `__objects` private class attribute is not of type
        dict
        """
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
        """Test ensure the dictionary returned by `all()` public
        instance method has values of type/subtype BaseModel.
        """
        for value in storage.all().values():
            self.assertIsInstance(value, BaseModel)

    def test_new(self):
        """Tests to ensure that public instance method `new(obj)`
        intended to add obj to the private class attribute `__objects`
        executes accordingly.
        """
        prev_count = len(storage.all())
        test_model_0 = BaseModel(
            id=str(uuid.uuid4()),
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        )
        storage.new(test_model_0)
        self.assertEqual(len(storage.all()), prev_count + 1)

    def test_new_accurate(self):
        """Tests to ensure that public instance method `new(obj)`
        intended to add obj to the private class attribute `__objects`
        stores the obj data accurately.
        """
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
            test_model_0.to_dict(),
        )

    def test_objects_key_format(self):
        """Test the format of all items in the dict stored as
        `__objects` private class attribute to ensure all keys follow format:
        "<class name>.id"
        """
        test_model_1 = BaseModel()
        test_model_2 = BaseModel()
        objs = storage.all()
        for key in storage.all().keys():
            self.assertEqual(key, f"{objs[key].__class__.__name__}.{objs[key].id}")

    def test_type(self):
        """type checks for FileStorage
        """
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_save(self):
        """Tests the FileStorage public instance method `save()`
        intended to save the current value of private class
        attribute `__objects` to the file specified by `__file_path`
        """
        with open("file.json", "r", encoding="utf-8") as myFile:
            dump = myFile.read()
        self.assertNotEqual(len(dump), 0)
        temp_d = eval(dump)
        key = self.temp_objs[0].__class__.__name__ + "."
        key += str(self.temp_objs[0].id)
        self.assertNotEqual(len(temp_d[key]), 0)
        key2 = "State.412409120491902491209491024"
        try:
            self.assertRaises(temp_d[key2], KeyError)
        except:
            pass

    def test_reload(self):
        """tests reload functionality for FileStorage"""
        storage.reload()
        obj_d = storage.all()
        key = self.temp_objs[1].__class__.__name__ + "."
        key += str(self.temp_objs[1].id)
        self.assertNotEqual(obj_d[key], None)
        self.assertEqual(obj_d[key].id, self.temp_objs[1].id)
        key2 = "State.412409120491902491209491024"
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass


if __name__ == "__main__":
    unittest.main()
