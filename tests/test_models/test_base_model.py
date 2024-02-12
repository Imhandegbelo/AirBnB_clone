#!/usr/bin/python3
"""
Test suits for the base model
"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests the attributes of the base model
    """
    def test_init(self):
        """
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Tests the save method
        """
        my_model = BaseModel()

        ini_updated_at = my_model.updated_at
        cur_updated_at = my_model.save()
        self.assertNotEqual(ini_updated_at, cur_updated_at)

    def setUp(self):
        """
        Classes needed for testing
        """
        pass

    def test_basic(self):
        """
        Tests basic inputs for the BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual(
                [my_model.name, my_model.number],
                ["ALX", 89])

    def test_to_dict(self):
        """
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(
                my_model_dict["created_at"],
                my_model.created_at.isoformat()
                )
        self.assertEqual(
                my_model_dict["updated_at"],
                my_model.updated_at.isoformat()
                )

    def test_str(self):
        """
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == '__main__':
    unittest.main()
