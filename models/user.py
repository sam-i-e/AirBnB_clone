#!/usr/bin/python3
"""Definition of the class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Details of the customer

    Args:
        BaseModel (class): the foundation of the application

    Attributes:
        email (str): Public class attribute for User's email
        password (str): Public class attribute for User's password
        first_name (str): Public class attribute for User's first name
        last_name (str): Public class attribute for User's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
