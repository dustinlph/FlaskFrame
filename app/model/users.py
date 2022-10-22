# coding=utf-8
"""
@Project: FlaskFrame
@File: app/model/users.py
@Author: Dustin Lin
@Created on: 2022/10/22 16:47:08
"""
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(256), unique=True)
	username = db.Column(db.String(64), unique=True)
	password_hash = db.Column(db.String(64), unique=True)
	created_at = db.Column(db.DateTime, server_default=func.now())

	def __repr__(self):
		return f"""id: {self.id}, username: {self.username}"""

	def as_dict(self):
		user = {u.name: getattr(self, u.name) for u in self.__table__.columns}
		user['created_at'] = user['created_at'].isoformat()
		return user

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)