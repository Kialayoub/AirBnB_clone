#!/usr/bin/python3
""" Review class """
from models.base_model import BaseModel

class Review(BaseModel):
    """ Attributes: place_id, user_id, text  """
    place_id = ""
    user_id = ""
    text = ""