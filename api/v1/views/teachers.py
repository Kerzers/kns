#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Teachers """
from models.teacher import Teacher
from models.user import User
from models.review import Review
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/teachers', methods=['GET'], strict_slashes=False)
def get_teachers():
    """
    Retrieves the list of all teacher objects
    """
    all_teachers = storage.all(Teacher).values()
    list_teachers= []
    for teacher in all_teachers:
        list_teachers.append(teacher.to_dict())
    return jsonify(list_teachers)


@app_views.route('/teachers/<teacher_id>', methods=['GET'], strict_slashes=False)
def get_teacher(teacher_id):
    """ Retrieves an teacher """
    teacher = storage.get(Teacher, teacher_id)
    if not teacher:
        abort(404)

    return jsonify(teacher.to_dict())


@app_views.route('/teachers/<teacher_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_teacher(teacher_id):
    """
    Deletes a teacher Object
    """
    teacher = storage.get(Teacher, teacher_id)

    if not teacher:
        abort(404)

    reviews = storage.all(Review)
    related_reviews = [review for review in reviews.values() if review.teacher_id == teacher.id]
    for review in related_reviews:
        storage.delete(review)

    storage.delete(teacher)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/teachers', methods=['POST'], strict_slashes=False)
def post_teacher():
    """
    Creates a teacher
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")
    if 'course_name' not in request.get_json():
        abort(400, description="Missing course")
    if 'description' not in request.get_json():
        abort(400, description="Missing description")

    data = request.get_json()
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    teacher_data = {'user_id': data['user_id'],
                    'description': data['description'],
                    'course_name': data['course_name'],
                    'user_name': user.user_name,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'location': user.location
    }

    instance = Teacher(**teacher_data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/teachers/<teacher_id>', methods=['PUT'], strict_slashes=False)
def put_teacher(teacher_id):
    """
    Updates a teacher
    """
    teacher = storage.get(Teacher, teacher_id)

    if not teacher:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(teacher, key, value)
    storage.save()
    return make_response(jsonify(teacher.to_dict()), 200)
