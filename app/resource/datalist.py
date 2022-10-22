# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/datalist.py
@Author: Dustin Lin
@Created on: 2022/10/23 02:38:52
"""
from flask import abort
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app.util.dto import DataDto
from app.model.data import Data as DataModel
from app.model.users import Users as UsersModel

data_api = DataDto.data_api
_data_get_response = DataDto.data_get_response


class DataListInfo(Resource):
	@jwt_required()
	@data_api.marshal_list_with(_data_get_response, code=200)
	def get(self, user_id):
		identity = get_jwt_identity()
		user = UsersModel.get_by_id(user_id)
		if user.username == identity:
			datalist = DataModel.get_data_list_by_user_id(user_id)
			return [d.as_dict() for d in datalist], 200
		else:
			abort(403, "Sorry! you can't do that.")
