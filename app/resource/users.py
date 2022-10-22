# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/users.py
@Author: Dustin Lin
@Created on: 2022/10/22 20:22:12
"""
from flask import abort
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from app.util.dto import UserDto
from app.model.users import Users as UsersModel

user_api = UserDto.user_api
_user_get_response = UserDto.user_get_response


class UserListInfo(Resource):
	@user_api.marshal_list_with(_user_get_response, code=200)
	@jwt_required()
	def get(self):
		users = UsersModel.get_user_list()
		return [u.as_dict() for u in users], 200

