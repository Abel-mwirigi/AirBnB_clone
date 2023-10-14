#!/usr/bin/python
""" holds the class State"""

from models.base_model import BaseModel

class State(BaseModel):
    """Represents state """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
