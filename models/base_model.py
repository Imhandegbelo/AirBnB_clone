#!/usr/bin/python3
"""
Module for the base class
- Public instance attributes:
    - id
    - createda_at
    - updated_at
- __str__ method to print
- public instamce methods
    - save(self) - updates updated_at
    - to_dict(self) - retuns dictionary from __dict__
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """
    The base model from which other class inherits
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of the object class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates updated_at with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary of __dict__ for an instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
