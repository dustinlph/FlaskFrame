# coding=utf-8
"""
@Project: FlaskFrame
@File: app/resource/__init__.py
@Author: Dustin Lin
@Created on: 2022/10/22 17:18:17
"""
from flask_restx import Api
from flask import Blueprint

from .auth import Login, Refresh
from .register import Register
from .user import User
from .users import UserListInfo
from .data import Data, CreateData
from .datalist import DataListInfo
from app.util.dto import AuthDto
from app.util.dto import RegisterDto
from app.util.dto import UserDto
from app.util.dto import DataDto
from app.config import api_version

api_blueprint = Blueprint("open_api", __name__, url_prefix="/api")

authorizations = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Add a jwt with ** Bearer token"
        }
    }

api = Api(
    api_blueprint, version=api_version, title='Swagger test', doc='/doc',
    description="hello swagger", prefix="/v1", authorizations=authorizations, security="Bearer Auth"
)

api.add_namespace(AuthDto.auth_api)
AuthDto.auth_api.add_resource(Login, '/login')
AuthDto.auth_api.add_resource(Refresh, '/refresh-token')

api.add_namespace(RegisterDto.register_api)
RegisterDto.register_api.add_resource(Register, '/register')

api.add_namespace(UserDto.user_api)
UserDto.user_api.add_resource(User, '/user/<int:user_id>')
UserDto.user_api.add_resource(UserListInfo, '/allusers')

api.add_namespace(DataDto.data_api)
DataDto.data_api.add_resource(Data, '/user/<int:user_id>/data/<int:data_id>')
DataDto.data_api.add_resource(CreateData, '/user/<int:user_id>/data')
DataDto.data_api.add_resource(DataListInfo, '/user/<int:user_id>/alldata')
