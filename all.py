#!/usr/bin/python3
""" Test create feature
"""
from models.engine.db_storage import DBStorage
from models.user import User

db = DBStorage()

# All Users
all_users = db.all(User)
print("All userss: {}".format(len(all_users.keys())))
# for user_key in all_users.keys():
    # print(all_users[user_key])
