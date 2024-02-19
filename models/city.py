#!/usr/bin/python3
"""Defines a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a class that inheirts from BaseModel
    public class attributes:
    state_id: string
    name: string
    """

    state_id = ""
    name = ""
