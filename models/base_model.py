#!/usr/bin/python3
"""defines all common attributes for other classes"""

import uuid
import datetime
from datetime import datetime
from models import storage

class BaseModel:
    """
    defines all common attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        """init method for Base model"""
        if  kwargs:
            for key, value in kwargs.items():
                  if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.__dict__.update(kwargs)
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            
            

    def __str__(self):
        """prints the string representation"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """dictionary containing all keys/values of __dict__"""
        dict = self.__dict__
        dict['__class__'] = str(type(self)).split('.')[-1].split('\'')[0]
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict