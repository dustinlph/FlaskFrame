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

from app.util.dto import AuthDto

auth_api = AuthDto.auth_api
_auth_request = AuthDto.auth_request
_auth_response = AuthDto.auth_response


class Login(Resource):
    @auth_api.marshal_with(_auth_response, code=200, description="OK")
    @auth_api.expect(_auth_request)
    def post(self):
        data = auth_api.payload
        username = data["username"]
        password = data["password"]

        if username != "test" or password != "test":
            return {"msg": "Bad username or password"}, 417

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return {"access_token": access_token, "refresh_token": refresh_token}, 200


class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {"access_token": access_token}
