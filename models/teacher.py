#!/usr/bin/python
""" holds class Teacher"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Teacher(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'teachers'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    description = Column(String(1024), nullable=False)
    course = Column(String(128), nullable=False)
  
    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)