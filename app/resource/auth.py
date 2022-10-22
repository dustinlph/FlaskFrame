# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/auth.py
@Author: Dustin Lin
@Created on: 2022/10/22 17:18:24
"""
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

auth_api = Namespace('auth', description="This is a description of authentication")

base_output_payload = auth_api.model('Basic output', {
    'status': fields.String(required=True, default=0),
    'message': fields.String(required=True, default="Response sample")
})

user_login_input_payload = auth_api.model('Register', {
    'username': fields.String(required=True, example="test"),
    'password': fields.String(required=True, example="test")
})

user_login_output_payload = auth_api.clone('Output of register', base_output_payload)


class Login(Resource):
    @auth_api.expect(user_login_input_payload)
    def post(self):
        data = auth_api.payload
        username = data["username"]
        password = data["password"]

        if username != "test" or password != "test":
            return {"msg": "Bad username or password"}, 401

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return {"access_token": access_token, "refresh_token": refresh_token}, 200


class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {"access_token": access_token}