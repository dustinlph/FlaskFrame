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
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

from .config import config_options
from app.model.users import Users as UsersModel
from app.resource import api_blueprint


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config_options[config_name])
	db.init_app(app)
	migrate = Migrate(app, db)
	jwt.init_app(app)
	app.register_blueprint(api_blueprint)

	return app
