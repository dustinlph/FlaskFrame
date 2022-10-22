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
from app.util.dto import AuthDto
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