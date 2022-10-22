# coding=utf-8
"""
@Project: FlaskFrame
@File: app/util/mail.py
@Author: Dustin Lin
@Created on: 2022/10/22 21:48:37
"""
from flask_mail import Message
from app import mail
from flask import current_app
from threading import Thread


def send_welcome_email(recipient: str):
	msg_title = "Welcome"
	msg_recipients: list = [recipient]
	msg_body = "Congrats. Register successfully"
	msg = Message(msg_title, recipients=msg_recipients)
	msg.body = msg_body
	thr = Thread(target=send_async_email, args=(current_app._get_current_object(), msg))
	thr.start()


def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)






