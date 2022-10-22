# coding=utf-8
"""
@Project: FlaskFrame
@File: app/config.py
@Author: Dustin Lin
@Created on: 2022/10/22 16:55:56
"""
import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
api_version = '0.0.2'


class Config():
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	JWT_SECRET_KEY = "super-secret"
	JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
	JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
	JWT_TOKEN_LOCATION = ['headers', 'query_string']
