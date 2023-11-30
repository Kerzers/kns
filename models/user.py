#!/usr/bin/python3
""" holds class User"""

from models.base_model import BaseModel, Base
#from models.teacher import Teacher
#from models.review import Review 
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5
# from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    email = Column(String(60), nullable=False)
    password = Column(String(128), nullable=False)
    user_name = Column(String(60), nullable=False)
    first_name = Column(String(60), nullable=True)
    last_name = Column(String(60), nullable=True)
    location = Column(String(60), nullable=True)
    user_discord= Column(String(60), nullable=True)
    user_wtsp = Column(String(60), nullable=True)

    teachers = relationship("Teacher", backref="user")
    reviews = relationship("Review", backref="user")
  
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)    
