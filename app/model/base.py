# coding=utf-8
"""
@Project: FlaskFrame
@File: app/model/base.py
@Author: Dustin Lin
@Created on: 2022/10/22 19:30:24
"""
from datetime import datetime

from app import db


class Base(db.Model):
	__abstract__ = True

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

	def add(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	@staticmethod
	def set_updated_at():
		return datetime.utcnow().replace(microsecond=0)
