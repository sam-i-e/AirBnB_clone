#!/usr/bin/python3
"""Definition of the class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Details of the City

    Args:
        BaseModel (class): foundation of the project

    Attributes:
        name (str): Public class attribute for City's name
        state_id (str): Public class attribute for City's state_id
    """

    state_id = ""
    name = ""
