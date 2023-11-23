#!/usr/bin/python
""" holds class Course"""
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Index
from sqlalchemy.orm import relationship


class Course(Base):
    """Representation of Course """
    __tablename__ = 'courses'
    name= Column(String(60), primary_key=True)
    teachers = relationship('Teacher', back_populates='course')

# Index('idx_courses_name', Course.name, unique=True)
