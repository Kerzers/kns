#!/usr/bin/python3
"""
Contains the TestDBStorage classes
"""

from datetime import datetime
import models
from models.engine import db_storage
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.teacher import Teacher
from models.course import Course
import json
import os
import unittest
from models import storage
DBStorage = db_storage.DBStorage
classes = {"Teacher": Teacher, "Course": Course, "Review": Review, "User": User}


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)
