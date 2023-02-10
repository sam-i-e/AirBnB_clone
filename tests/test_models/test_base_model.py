#!/usr/bin/python3
'''Test file for the 'BaseModel' class
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    '''TestBaseModelClass test class.
    '''

    def test_if_public_attribute(self):
        '''tests if the 'id', 'created_at' and 'updated_at' instance attributes
        are public instance attributes.
        '''
        base1 = BaseModel()
        with self.assertRaises(AttributeError):
            try:
                unique_id = base1.id
                time_created = base1.created_at
                time_updated = base1.updated_at
            except AttributeError:
                pass
            else:
                raise AttributeError

    def test_string_format(self):
        '''tests the format of the string representation of a 'BaseModel'
        object
        '''
        base1 = BaseModel()
        test_string = "[{}] ({}) {}".format(
                base1.__class__.__name__, base1.id, base1.__dict__
                )
        self.assertEqual(str(base1), test_string)

    def test_id_type(self):
        '''tests id's type to see if it's a string
        '''
        base1 = BaseModel()
        self.assertIs(type(base1.id), str)

    def test_current_datetime(self):
        '''tests if the 'created_at' and 'updated_at' attributes of a
        'BaseModel' instance are set to the current time.
        '''
        base1 = BaseModel()
        test_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_created = base1.created_at.strftime("%Y-%m-%d %H:%M:%S")
        time_updated = base1.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(time_created, test_datetime)
        self.assertEqual(time_updated, test_datetime)

    def test_id_exists_dict(self):
        '''tests if the 'id' element exists in the object's dictionary
        representation. and has a unique ID value
        '''
        base1 = BaseModel()
        obj_dict = base1.to_dict()
        self.assertIsNotNone(obj_dict['id'])
        self.assertIn('id', obj_dict.keys())

    def test_class_in_dict(self):
        '''tests if the '__class__' key was added to the dictionary
        representation of the 'BaseModel' object.
        '''
        base1 = BaseModel()
        obj_dict = base1.to_dict()
        self.assertIn('__class__', obj_dict.keys())

    def test_created_and_updated_time_format(self):
        '''tests the string format of the 'created_at' and 'updated_at'
        keys in the dictionary representation of the 'BaseModel' object.
        '''
        base1 = BaseModel()
        format_created = base1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        format_updated = base1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict = base1.to_dict()
        self.assertEqual(obj_dict['created_at'], format_created)
        self.assertEqual(obj_dict['updated_at'], format_updated)

    def test_updated_time(self):
        '''tests if the 'updated_at' attribute's value is updated whenever the
        save() function is called.
        '''
        base1 = BaseModel()
        prev_time = base1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        base1.save()
        curr_time = base1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.assertNotEqual(prev_time, curr_time)

    def test_initialization_using_kwargs(self):
        '''tests if 'BaseModel' object can be initiailised using a dictionary.
        '''
        init_dict = {
                        'id': '123456789',
                        'created_at': '2022-08-29T11:23:12.283000',
                        'updated_at': '2022-08-29T11:23:12.283000'
                    }
        base1 = BaseModel(**init_dict)
        base1_dict = base1.__dict__
        self.assertIs(type(base1.id), str)
        self.assertIs(type(base1.created_at), datetime)
        self.assertIs(type(base1.created_at), datetime)
        self.assertIsNotNone(base1.id)
        self.assertIsNotNone(base1.created_at)
        self.assertIsNotNone(base1.updated_at)
        self.assertNotIn('__class__', base1_dict.keys())


if __name__ == '__main__':
    unittest.main()
