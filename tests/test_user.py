#!/usr/bin/python3
""" Test create feature
"""
from models.engine.db_storage import DBStorage
from models.user import User

db = DBStorage()

# All Users
all_users = db.all(User)
print("All userss: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

# Create a new User
new_user = User()
new_user.email = "hi@world.com"
new_user.password = "hi"
new_user.user_name = "RitaHi"
db.new(new_user)
db.save()
print("New User: {}".format(new_user))

# All Users
all_users = db.all(User)
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

# Create another User
data = {"email": "marhaba@world.com", "password": "mar7aba", "user_name": "flodal"}
another_user = User(**data)
db.new(another_user)
db.save()
print("Another User: {}".format(another_user))

# All Users
all_users = db.all(User)
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])        

# Delete the new User
db.delete(new_user)

# All Users
all_users = db.all(User)
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

