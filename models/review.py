#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    stars = Column(Integer, nullable=False)
    username = Column(String(60), nullable=False)
  
    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
