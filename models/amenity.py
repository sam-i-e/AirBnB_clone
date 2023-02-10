#!/usr/bin/python3
"""Definition of the class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Name of the Amenity

    Args:
        BaseModel (class): Foundation of the project

    Attribute:
        name (str): Public class attribute for Amenity's name
    """

    name = ""
