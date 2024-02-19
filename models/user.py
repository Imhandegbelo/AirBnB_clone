#!/usr/bin/python3
"""Defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a class that inherits from BaseModel

        Public class attributes:
           email: string
           password: string
           first_name: string
           last_name: string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
