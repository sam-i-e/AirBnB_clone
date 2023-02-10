#!/usr/bin/python3
"""Definition of the class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reviews from the customer about the service

    Args:
        BaseModel (class): Foundation of the application

    Attributes:
        place_id (str): Public class attribute for Review's place_id
        user_id (str): Public class attribute for Review's user_id
        text (str): Public class attribute for Review's text
    """

    place_id = ""
    user_id = ""
    text = ""
