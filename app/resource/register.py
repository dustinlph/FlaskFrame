# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/register.py
@Author: Dustin Lin
@Created on: 2022/10/22 18:02:11
"""
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
		data = register_api.payload
		user = UsersModel(username=data["username"])
		user.set_password(data["password"])
		db.session.add(user)
		db.session.commit()
		return {"message": "Success", "username": data["username"]}, 201
