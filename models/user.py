#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel


class user(BaseModel):
    """Representation of state """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
