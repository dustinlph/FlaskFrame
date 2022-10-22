# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/user.py
@Author: Dustin Lin
@Created on: 2022/10/22 18:05:38
"""
from flask_restx import Resource

from app import db
from app.util.dto import UserDto
from app.model.users import Users as UsersModel

user_api = UserDto.user_api
_user_put_request = UserDto.user_put_request
_user_get_response = UserDto.user_get_response


class User(Resource):
	@user_api.marshal_with(_user_get_response, code=200)
	def get(self, id):
		user = db.session.query(UsersModel).filter(
			UsersModel.id == id
		).first()
		return {"username": user.username, "id": user.id}, 200

	@user_api.expect(_user_put_request)
	def put(self, id):
		data = user_api.payload
		user = db.session.query(UsersModel).filter(
			UsersModel.id == id
		).first()
		user.username = data["username"]
		user.set_password(data["password"])
		db.session.commit()
		return {"message": "success"}, 200

	def delete(self, id):
		user = db.session.query(UsersModel).filter(
			UsersModel.id == id
		).first()
		db.session.delete(user)
		db.session.commit()
		return {"message": "success"}, 200
