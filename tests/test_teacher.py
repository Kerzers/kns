#!/usr/bin/python3
""" Test create feature
"""
from models.engine.db_storage import DBStorage
from models.teacher import Teacher

db = DBStorage()

# All Teachers
all_teachers = db.all(Teacher)
print("All teachers: {}".format(len(all_teachers.keys())))
for teacher_key in all_teachers.keys():
    print(all_teachers[teacher_key])

# Create a new Teacher
new_teacher = Teacher()
new_teacher.user_id = 'e9d43546-e0f6-4ddb-9ce8-8b939a31e1b8' 
new_teacher.course= "Football"
new_teacher.description= "Hello I am an expiremented trainer in football..."
db.new(new_teacher)
db.save()
print("New Teacher: {}".format(new_teacher))

# All Teachers
all_teachers = db.all(Teacher)
print("All Teachers: {}".format(len(all_teachers.keys())))
for teacher_key in all_teachers.keys():
    print(all_teachers[teacher_key])

# Create another Teacher
data = {"user_id": "41158e32-a18f-485f-ab0a-ce986ca80181", "course": "Python", "description": "I am number 1"}
another_teacher = Teacher(**data)
db.new(another_teacher)
db.save()
print("Another Teacher: {}".format(another_teacher))

# All Teachers
all_teachers = db.all(Teacher)
print("All Teachers: {}".format(len(all_teachers.keys())))
for teacher_key in all_teachers.keys():
    print(all_teachers[teacher_key])        

# Delete the new Teacher
db.delete(new_teacher)

# All Teachers
all_teachers = db.all(Teacher)
print("All Teachers: {}".format(len(all_teachers.keys())))
for teacher_key in all_teachers.keys():
    print(all_teachers[teacher_key])

