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
	title = db.Column(db.String(64), unique=False)
	info = db.Column(db.String(256), unique=False)
	created_at = db.Column(db.DateTime, server_default=func.now())
	updated_at = db.Column(db.DateTime, server_default=func.now())

	def __repr__(self):
		return f"""id: {self.id}, username: {self.username}"""

	def as_dict(self):
		data = {d.name: getattr(self, d.name) for d in self.__table__.columns}
		data['created_at'] = data['created_at'].isoformat()
		data['updated_at'] = data['updated_at'].isoformat()
		return data

	@staticmethod
	def get_by_user_id_data_id(user_id, data_id):
		return db.session.query(Data).filter(
			Data.id == data_id,
			Data.user_id == user_id
		).first()

	@staticmethod
	def get_data_list_by_user_id(user_id):
		return db.session.query(Data).filter(
			Data.user_id == user_id
		).all()
