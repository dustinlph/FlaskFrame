# coding=utf-8
"""
@Project: FlaskFrame
@File: app/__init__.py
@Author: Dustin Lin
@Created on: 2022/10/22 16:37:24
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint
from flask_restx import Api
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

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
	api_blueprint, version='0.0.1', title='Swagger test', doc='/doc',
	description="hello swagger", prefix="/v1", authorizations=authorizations, security="Bearer Auth"
)

from .config import Config
from app.model.users import Users as UsersModel


def register_api():
	from .resource.auth import auth_api, Login, Refresh

	api.add_namespace(auth_api)
	auth_api.add_resource(Login, '/login')
	auth_api.add_resource(Refresh, '/refresh-token')


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	migrate = Migrate(app, db)
	jwt.init_app(app)
	register_api()
	app.register_blueprint(api_blueprint)

	return app
