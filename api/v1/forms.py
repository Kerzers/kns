#!/usr/bin/python3
"""module of forms"""
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models.user import User
from models import storage


class SignupForm(FlaskForm):
    """Class to handle sign up form"""
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Check if the username is already in use"""
        all_users = storage.all(User).values()
        for user in all_users:
            if username.data == user.user_name:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """Check if the email is already in use"""
        all_users = storage.all(User).values()
        for user in all_users:
            if email.data == user.email:
                raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """Class to handle login form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
