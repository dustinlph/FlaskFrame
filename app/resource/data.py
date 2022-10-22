# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/data.py
@Author: Dustin Lin
@Created on: 2022/10/23 00:47:27
"""
from flask import abort
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app.util.dto import DataDto
from app.model.data import Data as DataModel
from app.model.users import Users as UsersModel

data_api = DataDto.data_api
_data_post_request = DataDto.data_post_request
_data_put_request = DataDto.data_put_request
_data_post_response = DataDto.data_post_response
_data_get_response = DataDto.data_get_response
_data_other_response = DataDto.data_other_response


class Data(Resource):
	@jwt_required()
	@data_api.marshal_with(_data_get_response, code=200)
	def get(self, user_id, data_id):
		identity = get_jwt_identity()
		user = UsersModel.get_by_id(user_id)
		data = DataModel.get_by_user_id_data_id(user_id, data_id)
		if user.username == identity:
			data = DataModel.get_by_user_id_data_id(user_id, data_id)
			return {"id": data.id, "title": data.title, "info": data.info}, 200
		else:
			abort(403, "Sorry! you can't do that.")

	@jwt_required()
	@data_api.marshal_with(_data_other_response)
	@data_api.expect(_data_put_request)
	def put(self, user_id, data_id):
		request_data = data_api.payload
		identity = get_jwt_identity()
		user = UsersModel.get_by_id(user_id)
		data = DataModel.get_by_user_id_data_id(user_id, data_id)
		if user.username == identity:
			data.title = request_data["title"] if data.title != request_data['title'] else data.title
			data.info = request_data["info"] if data.info != request_data["info"] else data.info
			DataModel.update(data)
			return {"message": "success"}, 200
		else:
			abort(403, "Sorry! you can't do that.")

	@jwt_required()
	@data_api.marshal_with(_data_other_response)
	def delete(self, user_id, data_id):
		identity = get_jwt_identity()
		user = UsersModel.get_by_id(user_id)
		data = DataModel.get_by_user_id_data_id(user_id, data_id)
		if user.username == identity:
			DataModel.delete(data)
			return {"message": "success"}, 200
		else:
			abort(403, "Sorry! you can't do that.")


class CreateData(Resource):
	@jwt_required()
	@data_api.marshal_with(_data_post_response, code=200)
	@data_api.expect(_data_post_request)
	def post(self, user_id):
		identity = get_jwt_identity()
		user = UsersModel.get_by_id(user_id)
		required_params: list = ['title', 'info']
		request_data = data_api.payload
		request_data_key: list = list(request_data.keys())
		missing_key = list()
		for i in range(len(required_params)):
			if required_params[i] in request_data_key:
				pass
			else:
				missing_key.append(required_params[i])
		if len(missing_key) != 0:
			abort(417, f"missing something: {missing_key}")

		if user.username == identity:
			data = DataModel(user_id=user_id, title=request_data["title"], info=request_data["info"])
			data.add()
			return {"message": "success", "id": data.id, "title": request_data["title"], "info": request_data["info"]}, 200
		else:
			abort(403, "Sorry! you can't do that.")
