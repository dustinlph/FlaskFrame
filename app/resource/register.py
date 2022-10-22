# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/register.py
@Author: Dustin Lin
@Created on: 2022/10/22 18:02:11
"""
from flask import abort
from flask_restx import Resource

from app import db
from app.util.dto import RegisterDto
from app.model.users import Users as UsersModel

register_api = RegisterDto.register_api
_register_request = RegisterDto.register_request
_register_response = RegisterDto.register_response

class Register(Resource):
	@register_api.marshal_with(_register_response, code=201)
	@register_api.expect(_register_request)
	def post(self):
		required_params: list = ['username', 'email', 'password']
		data = register_api.payload
		data_key: list = list(data.keys())
		missing_key = list()
		for i in range(len(required_params)):
			if required_params[i] in data_key:
				pass
			else:
				missing_key.append(required_params[i])
		if len(missing_key) != 0:
			abort(417, f"missing something: {missing_key}")

		user = UsersModel(username=data["username"])
		user.set_password(data["password"])
		user.add()
		return {"message": "Success", "username": data["username"]}, 201
