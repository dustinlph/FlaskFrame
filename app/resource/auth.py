# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/auth.py
@Author: Dustin Lin
@Created on: 2022/10/22 17:18:24
"""
from flask import abort
from flask_restx import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from app.util.dto import AuthDto
from app.model.users import Users as UsersModel

auth_api = AuthDto.auth_api
_auth_request = AuthDto.auth_request
_auth_response = AuthDto.auth_response


class Login(Resource):
    @auth_api.marshal_with(_auth_response, code=200, description="OK")
    @auth_api.expect(_auth_request)
    def post(self):
        data = auth_api.payload
        login_user = UsersModel.get_by_username(data["username"])
        if login_user:
            if login_user.check_password(data["password"]):
                access_token = create_access_token(identity=data["username"])
                refresh_token = create_refresh_token(identity=data["username"])
                return {"access_token": access_token, "refresh_token": refresh_token}, 200
            abort(401, "Password incorrect")
        abort(400, "User not found")


class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {"access_token": access_token}
