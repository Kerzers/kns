#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Reviews """
from models.review import Review
from models.teacher import Teacher
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def get_reviews():
    """
    Retrieves the list of all review objects
    """
    all_reviews = storage.all(Review).values()
    list_reviews= []
    for review in all_reviews:
        list_reviews.append(review.to_dict())
    return jsonify(list_reviews)


@app_views.route('/teachers/<teacher_id>/reviews', methods=['GET'], strict_slashes=False)
def get_review(teacher_id):
    """ Retrieves the list of reviews of a teacher"""
    teacher = storage.get(Teacher, teacher_id)
    if not teacher:
        abort(404)
    
    reviews = [review.to_dict() for review in teacher.reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """
    Deletes a review Object
    """
    review = storage.get(Review, review_id)

    if not review:
        abort(404)

    storage.delete(review)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/teachers/<teacher_id>/reviews', methods=['POST'], strict_slashes=False)
def post_review(teacher_id):
    """
    Creates a review for a teacher
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")
    if 'stars' not in request.get_json():
        abort(400, description="Missing stars")
    if 'text' not in request.get_json():
         abort(400, description="Missing review")
 
    data = request.get_json()
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)

    teacher = storage.get(Teacher, teacher_id)
    if not teacher:
        abort(404)

    if user.id == teacher.user_id:
        abort(400, description="You can not review yourself!")
    data['teacher_id'] = teacher_id
    instance = Review(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """
    Updates a review
    """
    review = storage.get(Review, review_id)

    if not review:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(review, key, value)
    storage.save()
    return make_response(jsonify(review.to_dict()), 200)
