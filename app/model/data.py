# coding=utf-8
"""
@Project: FlaskFrame
@File: app/model/data.py
@Author: Dustin Lin
@Created on: 2022/10/22 22:28:08
"""
from sqlalchemy.sql import func

from app import db
from app.model.base import Base


class Data(Base):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	title = db.Column(db.String(64), unique=True)
	Info = db.Column(db.String(256), unique=True)
	created_at = db.Column(db.DateTime, server_default=func.now())
	updated_at = db.Column(db.DateTime, server_default=func.now())

	def __repr__(self):
		return f"""id: {self.id}, username: {self.username}"""

	def as_dict(self):
		data = {d.name: getattr(self, d.name) for d in self.__table__.columns}
		data['created_at'] = data['created_at'].isoformat()
		data['updated_at'] = data['updated_at'].isoformat()
		return data
