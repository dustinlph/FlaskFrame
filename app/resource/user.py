# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/user.py
@Author: Dustin Lin
@Created on: 2022/10/22 18:05:38
"""
from flask import abort
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app.util.dto import UserDto
from app.model.users import Users as UsersModel

user_api = UserDto.user_api
_user_put_request = UserDto.user_put_request
_user_get_response = UserDto.user_get_response


class User(Resource):
	@jwt_required()
	@user_api.marshal_with(_user_get_response, code=200)
	def get(self, user_id):
		user = UsersModel.get_by_id(user_id)
		if user:
			return {"username": user.username, "id": user.id}, 200
		return {"message": "user not found"}

	@jwt_required()
	@user_api.expect(_user_put_request)
	def put(self, user_id):
		data = user_api.payload
		identity = get_jwt_identity()
		user = UsersModel.get_by_id(user_id)
		if user.username == identity:
			user.username = data["username"] if user.username != data['username'] else user.username
			user.email = data["email"] if user.email != data["email"] else user.email
			UsersModel.update(user)
			return {"message": "success"}, 200
		else:
			abort(403, "Sorry! you can't do that.")

	@jwt_required()
	def delete(self, user_id):
		identity = get_jwt_identity()
		user = UsersModel.get_by_id(user_id)
		if user.username == identity:
			UsersModel.delete(user)
			return {"message": "success"}, 200
		else:
			abort(403, "Sorry! you can't do that.")
