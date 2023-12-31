#!/usr/bin/python3
"""falsk app"""
from flask import Flask, render_template, url_for, flash, redirect, make_response, jsonify
from api.v1.forms import SignupForm, LoginForm
from api.v1.views import app_views
from os import environ
import models
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import storage
from models.user import User
from flask_wtf.csrf import CSRFProtect
from hashlib import md5


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
csrf = CSRFProtect(app)
cors = CORS(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    """
    return make_response(jsonify({'error': "Not found"}), 404)

@app.route("/sign_up", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    hash_password = md5((form.password.data).encode()).hexdigest()
    if form.validate_on_submit():
        dic = {"email": form.email.data, "password": form.password.data, "user_name": form.username.data}
        user = User(**dic)
        user.save()
        return jsonify({'message': 'Account created successfuly', "id": user.id})
    
    else:
        for field, errors in form.errors.items():
            errors = {field: [str(error) for error in errors]}
        return jsonify({'message': 'Validation failed', 'errors': errors}), 400

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    all_users = storage.all(User).values()
    for user in all_users:
        if user.email == form.email.data:
            if user.password == md5((form.password.data).encode()).hexdigest():
                return jsonify({'message': 'success', "id": user.id})
            else:
                return jsonify({'message': 'password not correct'})
    return jsonify({'message': 'email not found'})

if __name__ == "__main__":
    """ Main Function """
    host = environ.get('KNS_API_HOST')
    port = environ.get('KNS_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(debug=True, host=host, port=port, threaded=True)
