#!/usr/bin/python3
""" Test create course feature
"""
from models.engine.db_storage import DBStorage
from models.course import Course

db = DBStorage()

# Create a new Course
new_course = Course()
new_course.name = "Python"
db.new(new_course)
db.save()
print("New Course: {}".format(new_course))
