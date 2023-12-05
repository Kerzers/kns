#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models.teacher import Teacher
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves the list of all user objects
    """
    storage.reload()
    all_users = storage.all(User).values()
    storage.close()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    storage.close()
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves an user """
    storage.reload()
    user = storage.get(User, user_id)
    if not user:
        storage.close()
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a user Object
    """
    storage.reload()
    user = storage.get(User, user_id)

    if not user:
        storage.close()
        abort(404)

    storage.delete(user)
    storage.save()
    storage.close()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """
    Updates a user
    """
    try:

        storage.reload()
        user = storage.get(User, user_id)
        if not user:
            abort(404)
            if not request.get_json():
                abort(400, description="Not a JSON")
        data = request.get_json()
        teachers = storage.all(Teacher).values()
        teacher = None
        for t in teachers:
            if t.user_id == user_id:
                teacher = t
                break
        
        ignore = ['id', 'email', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in ignore:
                setattr(user, key, value)
                if teacher:
                    setattr(teacher, key, value)
        storage.save()
        return make_response(jsonify(user.to_dict()), 200)
    except Exception as e:
        print(f"An error occurred: {e}")
        abort(500)
    finally:
        storage.close()
