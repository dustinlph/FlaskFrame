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

db = SQLAlchemy()

from .config import Config
from app.model.users import Users as UsersModel

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	migrate = Migrate(app, db)

	return app

