#!/usr/bin/python3
""" User class """
from models.base_model import BaseModel

class User(BaseModel):
    """ Attributes: email, password, first_name and last_name """
    email = ""
    password = ""
    first_name = ""
    last_name = ""