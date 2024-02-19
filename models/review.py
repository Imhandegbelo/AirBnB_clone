#!/usr/bin/python3
"""Defines a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a class that inherits from BaseModel

    public class attributes:
    place_id: string
    user_id: string
    text: sting
    """

    place_id = ""
    user_id = ""
    text = ""
