# coding=utf-8
"""
@Project: FlaskFrame
@File: app/config.py
@Author: Dustin Lin
@Created on: 2022/10/22 16:55:56
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
