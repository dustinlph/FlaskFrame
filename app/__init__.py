# coding=utf-8
"""
@Project: FlaskFrame
@File: app/__init__.py
@Author: Dustin Lin
@Created on: 2022/10/22 16:37:24
"""
from flask import Flask


def create_app():
	app = Flask(__name__)
	return app

