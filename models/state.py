#!/usr/bin/python3
"""Definition of the class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Name of the State

    Args:
        BaseModel (class): the foundation of the application

    Attribute:
        name (str): Public class attribute for State's name
    """

    name = ""
