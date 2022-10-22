# coding=utf-8
"""
@Project: FlaskFrame
@File: app/util/dto.py
@Author: Dustin Lin
@Created on: 2022/10/22 17:37:41
"""
from flask_restx import Namespace, fields


class AuthDto:
    auth_api = Namespace('auth', description="This is a description of authentication")
    auth_request = auth_api.model('auth_request', {
        "username": fields.String(required=True, description='enter username', example="test"),
        "password": fields.String(required=True, description="enter password", example="test")
    })
    auth_response = auth_api.model('auth_response', {
        "access_token": fields.String(example="access token"),
        "refresh_token": fields.String(example="refresh token")
    })


class RegisterDto:
    register_api = Namespace('user', description="This is a desc. of user")
    # path='/' -> endpoint: /{set value in add_resource()}
    register_request = register_api.model('register_request', {
        "username": fields.String(required=True, description="please set your username", example="Doe"),
        "email": fields.String(requried=True, description="please enter your email address", example="doe@demo.demo"),
        "password": fields.String(required=True, description="please set your password", example="Doe!123#")
    })
    register_response = register_api.model('register_response', {
        "message": fields.String(example="Success"),
        "username": fields.String(example="Doe")
    })


class UserDto:
    user_api = Namespace('user', path='/')
    user_put_request = user_api.model('user_request', {
        "username": fields.String(required=False, description="name you want to change", example="Doe"),
        "email": fields.String(required=False, description="enter the new email", example="demo@demo.demo")
    })
    user_get_response = user_api.model('user_response', {
        "id": fields.Integer(),
        "username": fields.String()
    })


class DataDto:
    data_api = Namespace('user', path='/')
    data_post_request = data_api.model('data_request', {
        "title": fields.String(required=True, description="Enter title", example="Title"),
        "info": fields.String(required=True, description="Enter info", example="The data info..."),
    })
    data_put_request = data_api.model('data_request', {
        "title": fields.String(required=False, description="Enter title", example="Title"),
        "info": fields.String(required=False, description="Enter info", example="The data info..."),
    })
    data_get_response = data_api.model('data_get_response', {
        "id": fields.Integer(),
        "title": fields.String(example="Data title"),
        "info": fields.String(example="Data info")
    })
    data_other_response = data_api.model("data_other_response", {
         "message": fields.String(example="success")
    })
    data_post_response = data_api.model("data_post_response", {
        "message": fields.String(example="success"),
        "id": fields.Integer(),
        "title": fields.String(example="Data title"),
        "info": fields.String(example="Data info")
    })
