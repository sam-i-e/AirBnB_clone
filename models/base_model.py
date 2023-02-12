#!/usr/bin/python3
"""Define the Base of the application"""

import uuid
from datetime import datetime

from models import storage


class BaseModel:
    """Methods and attributes of the project"""

    def __init__(self, *args, **kwargs):
        """
        Initialize the project attributes

        Attributes:
            args (list): inputted arguments as a list.
            kwargs (dict): inputted arguments as a dict.
            id (str) - assign with an uuid when an instance is created.
            created_at (time): datetime - assign with the current datetime when
                an instance is created.
            updated_at (time): datetime - assign with the current datetime when
                n instance is created and it will be updated every time you
                change your object.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        String representation of the Base model
        Return:
            string (str): string description for BaseModel class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save and update the public attribute `updated_at` with current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        serialization of object by returning the dictionary of the object
        Return:
            result (dict): Dictionary object that contains __dict__
        """
        result = self.__dict__.copy()
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["__class__"] = self.__class__.__name__
        return result
