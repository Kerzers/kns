#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Teachers """
from models.teacher import Teacher
from models.user import User
from models.review import Review
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/teachers/<teacher_id>', methods=['GET'], strict_slashes=False)
@app_views.route('/teachers', methods=['GET'], strict_slashes=False)
def get_teachers(teacher_id=None):
    """Retrieves the list of all teacher objects"""
    try:
        storage.reload()
        
        all_teachers = storage.all(Teacher).values()
        list_teachers= [teacher.to_dict() for teacher in all_teachers]
        
        if teacher_id is None:
            return jsonify(list_teachers)
        else:
            for elmt in list_teachers:
                if elmt["id"] == teacher_id:
                    return jsonify(elmt)
            abort(404)
    except Exception as e:
        storage.rollback()
        abort(400, description=str(e))
    finally:
        storage.close()


@app_views.route('/teachers/<teacher_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_teacher(teacher_id):
    """
    Deletes a teacher Object
    """
    try:
        storage.reload()
        teacher = storage.get(Teacher, teacher_id)

        if not teacher:
            abort(404)

        reviews = storage.all(Review)
        related_reviews = [review for review in reviews.values() if review.teacher_id == teacher.id]
        for review in related_reviews:
            storage.delete(review)

        storage.delete(teacher)
        storage.save()
    except Exception as e:
        storagerollback()
        abort(400, description=str(e))
    finally:
        storage.close()

    return make_response(jsonify({}), 200)


@app_views.route('/teachers', methods=['POST'], strict_slashes=False)
def post_teacher():
    """
    Creates a teacher
    """
    try:
        if not request.get_json():
            abort(400, description="Not a JSON")

        if 'user_id' not in request.get_json():
            abort(400, description="Missing user_id")
        if 'course_name' not in request.get_json():
            abort(400, description="Missing course")
        if 'description' not in request.get_json():
            abort(400, description="Missing description")

        data = request.get_json()

        storage.reload()
        user = storage.get(User, data['user_id'])
        if not user:
            abort(404)
        teacher_data = {'user_id': data['user_id'],
                        'description': data['description'],
                        'course_name': data['course_name'],
                        'user_name': user.user_name,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'user_email': user.email,
                        'user_discord': user.user_discord,
                        'user_wtsp': user.user_wtsp,
                        'location': user.location
        }   
        print(f"this is teacher data {teacher_data}")

        instance = Teacher(**teacher_data)
        instance.save()
    except Exception as e:
        storage.rollback()
        abort(400, description=str(e))
    finally:
        storage.close()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/teachers/<teacher_id>', methods=['PUT'], strict_slashes=False)
def put_teacher(teacher_id):
    """
    Updates a teacher
    """
    try:
        storage.reload()
        teacher = storage.get(Teacher, teacher_id)

        if not teacher:
            abort(404)

        if not request.get_json():
            abort(400, description="Not a JSON")

        required_fields = ['course_name', 'description']
        data = request.get_json()
        if not all(field in data for field in required_fields):
            abort(400, description="Missing required fields: {}".format(', '.join(required_fields)))
        
        for key, value in data.items():
            if key in required_fields:
                setattr(teacher, key, value)
        
        storage.save()
    except Exception as e:
        storage.rollback()
        abort(400, description=str(e))
    finally:
        storage.close()
    return make_response(jsonify(teacher.to_dict()), 200)

@app_views.route('/teachers_search', methods=['POST'], strict_slashes=False)
def teachers_search():
    """
    Retrieves all Teacher objects depending of the course name of the request
    """
    try:
        if request.get_json() is None:
            abort(400, description="Not a JSON")

        data = request.get_json()
        list_teachers = []

        storage.reload()
        if 'course_name' in data:
            course_name = data['course_name']
            all_teachers = storage.all(Teacher).values()

            # Filter teachers based on the course name
            for teacher in all_teachers:
                if course_name in teacher.course_name:
                    list_teachers.append(teacher.to_dict())
            return jsonify(list_teachers)

        # If 'course_name' is not provided, return all teachers
        all_teachers = storage.all(Teacher).values()
        for teacher in all_teachers:
            list_teachers.append(teacher.to_dict())
        return jsonify(list_teachers)
    except Exception as e:
        storage.rollback()
        abort(400, description=str(e))
    finally:
            storage.close()
