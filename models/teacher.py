#!/usr/bin/python
""" holds class Teacher"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Teacher(BaseModel, Base):
    """Representation of Teacher """
    __tablename__ = 'teachers'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user_name = Column(String(60))
    first_name = Column(String(60))
    last_name = Column(String(60))
    location = Column(String(60))
    description = Column(String(1024), nullable=False)
    course_name = Column(String(60), ForeignKey('courses.name'))
    course = relationship('Course', back_populates='teachers')
    reviews = relationship('Review', back_populates='teachers', cascade='all, delete-orphan')
  
    def __init__(self, *args, **kwargs):
        """initializes teacher """
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        from models.review import Review
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.teacher_id == self.id:
                review_list.append(review)
        return review_list
